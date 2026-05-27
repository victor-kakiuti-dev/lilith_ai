from fastapi import APIRouter
from app.models.chat_models import ChatRequest
from app.services.openai_service import generate_response

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    response = generate_response(
        request.user_id,
        request.message
        )

    return {
        "response": response
    }