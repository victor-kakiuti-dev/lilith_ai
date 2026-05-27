from fastapi import APIRouter, Request
import requests
import os

from app.services.openai_service import generate_response

router = APIRouter()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

@router.post("/webhook")
async def telegram_webhook(request: Request):

    data = await request.json()

    message = data["message"]["text"]

    chat_id = data["message"]["chat"]["id"]

    response = generate_response(
        str(chat_id),
        message
    )

    send_message(chat_id, response)

    return {"ok": True}

def send_message(chat_id, text):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    requests.post(url, json=payload)