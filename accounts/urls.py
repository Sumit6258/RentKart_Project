from django.urls import path
from .views import send_otp_api, verify_otp_view, customer_signup, customer_login, forgot_password, reset_password

urlpatterns = [
    path('send-otp/', send_otp_api),
    path('signup/', customer_signup),
    path('login/', customer_login),
    path('forgot-password/', forgot_password),
    path('reset-password/', reset_password),
]
