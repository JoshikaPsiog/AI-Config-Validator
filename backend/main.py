from fastapi import FastAPI
from routes.repository import router as repository_router
from routes.upload import router as upload_router
from routes.read import router as read_router
from routes.validate import router as validate_router
from fastapi.middleware.cors import CORSMiddleware
from ai.gemini_service import ask_gemini
from ai.ollama_service import ask_ollama
app = FastAPI(
    title="AI-Driven Configuration Validation System",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "AI Config Validator Running"
    }

# Register Routes
app.include_router(upload_router)
app.include_router(read_router)
app.include_router(validate_router)
app.include_router(repository_router)

@app.get("/ai-test")
def ai_test():

    answer = ask_gemini(
        "Explain why enabling S3 bucket encryption is important in Terraform."
    )

    return {
        "response": answer
    }


@app.get("/ollama-test")
def ollama_test():

    answer = ask_ollama(
        "Explain why an S3 bucket should not be public in Terraform."
    )

    return {
        "response": answer
    }
    return {
        "response": answer
    }