from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai.prompt_builder import build_security_prompt
from ai.groq_service import ask_groq
from ai.ollama_service import ask_ollama

router = APIRouter()


class RecommendationRequest(BaseModel):
    reason: str


@router.post("/recommend")
def recommend(request: RecommendationRequest):

    prompt = build_security_prompt(request.reason)

    try:
        # Try Groq first
        answer = ask_groq(prompt)

        return {
            "provider": "Groq",
            "recommendation": answer
        }

    except Exception:

        # Automatic fallback to Ollama
        answer = ask_ollama(prompt)

        return {
            "provider": "Ollama",
            "recommendation": answer
        }