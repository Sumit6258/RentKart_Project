import time

OTP_STORE = {}

def save_otp(phone, otp):
    OTP_STORE[phone] = {
        "otp": otp,
        "timestamp": time.time()
    }

def verify_otp(phone, otp, expiry=600):
    data = OTP_STORE.get(phone)
    if not data:
        return False

    if time.time() - data["timestamp"] > expiry:
        return False

    return data["otp"] == otp
