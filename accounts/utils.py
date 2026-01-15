import random
import requests
import os

def send_otp(phone):
    otp = random.randint(100000, 999999)

    message = f"Rentkart OTP for {phone} is {otp}"

    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
    payload = {
        "chat_id": os.getenv("TELEGRAM_CHAT_ID"),
        "text": message
    }

    requests.post(url, json=payload)
    return otp
