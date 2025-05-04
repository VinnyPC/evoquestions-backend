from fastapi import APIRouter
from app.models.prompt_request import PromptRequest
from app.services.gemini_service import gerar_pergunta_gemini

router = APIRouter()

@router.post("/gerar-pergunta")
async def gerar_pergunta(prompt_req: PromptRequest):
    return await gerar_pergunta_gemini(prompt_req.topic)
