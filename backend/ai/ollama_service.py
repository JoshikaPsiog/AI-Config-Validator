import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://127.0.0.1:11434/api/generate"
)


def ask_ollama(prompt: str):

    payload = {
        "model": "llama3.1:8b",
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "No response from Ollama.")

    except Exception as e:

        return f"Ollama Error: {str(e)}"