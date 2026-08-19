import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"


def ask_ollama(prompt):

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "").strip()

    except requests.exceptions.RequestException as e:

        return f"Ollama Error: {e}"

    except Exception as e:

        return f"Ollama Error: {e}"