from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Customer
from .utils import send_otp

from .otp_store import save_otp

OTP_STORE = {}

@api_view(['POST'])
def send_otp_api(request):
    phone = request.data.get('phone')

    otp = send_otp(phone)
    save_otp(phone, otp)

    return Response({"message": "OTP sent successfully"})


@api_view(['POST'])
def verify_otp_view(request):
    phone = request.data.get('phone')
    otp = int(request.data.get('otp'))

    if OTP_STORE.get(phone) == otp:
        user, created = User.objects.get_or_create(phone=phone)

        # Customer auto-create
        customer, _ = Customer.objects.get_or_create(
            phone=phone,
            defaults={"name": f"Customer {phone[-4:]}"}
        )

        return Response({
            "message": "Login successful",
            "is_admin": user.is_staff,
            "customer_id": customer.id,
            "phone": phone
        })

    return Response({"error": "Invalid OTP"}, status=400)


@api_view(['POST'])
def customer_signup(request):
    phone = request.data.get('phone')
    otp = int(request.data.get('otp'))
    name = request.data.get('name')
    email = request.data.get('email')

    from .otp_store import verify_otp

    if not verify_otp(phone, otp):
        return Response({"error": "Invalid or expired OTP"}, status=400)

    customer, created = Customer.objects.get_or_create(
        phone=phone,
        defaults={"name": name, "email": email, "is_verified": True}
    )

    return Response({
        "message": "Account created successfully",
        "customer_id": customer.id
    })


@api_view(['POST'])
def customer_signup(request):
    phone = request.data.get('phone')
    otp = int(request.data.get('otp'))
    name = request.data.get('name')
    email = request.data.get('email')

    from .otp_store import verify_otp

    if not verify_otp(phone, otp):
        return Response({"error": "Invalid or expired OTP"}, status=400)

    customer, created = Customer.objects.get_or_create(
        phone=phone,
        defaults={"name": name, "email": email, "is_verified": True}
    )

    return Response({
        "message": "Account created successfully",
        "customer_id": customer.id
    })


@api_view(['POST'])
def customer_login(request):
    phone = request.data.get('phone')
    otp = int(request.data.get('otp'))

    from .otp_store import verify_otp

    if not verify_otp(phone, otp):
        return Response({"error": "Invalid OTP"}, status=400)

    customer = Customer.objects.filter(phone=phone, is_verified=True).first()
    if not customer:
        return Response({"error": "Account not found"}, status=404)

    return Response({
        "message": "Login successful",
        "customer_id": customer.id
    })


@api_view(['POST'])
def forgot_password(request):
    phone = request.data.get('phone')

    if not Customer.objects.filter(phone=phone).exists():
        return Response({"error": "Phone not registered"}, status=404)

    otp = send_otp(phone)
    save_otp(phone, otp)

    return Response({"message": "OTP sent for password reset"})


@api_view(['POST'])
def reset_password(request):
    phone = request.data.get('phone')
    otp = int(request.data.get('otp'))
    new_password = request.data.get('new_password')

    from .otp_store import verify_otp

    if not verify_otp(phone, otp):
        return Response({"error": "Invalid OTP"}, status=400)

    customer = Customer.objects.get(phone=phone)
    customer.set_password(new_password)
    customer.save()

    return Response({"message": "Password reset successful"})
