from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.telegram import router as telegram_router


app = FastAPI()

app.include_router(telegram_router)

app.include_router(chat_router)

