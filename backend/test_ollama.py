from ai.ollama_service import ask_ollama
from ai.prompt_builder import build_prompt

prompt = build_prompt(
    "aws_s3_bucket.public_bucket",
    "S3 bucket is publicly accessible"
)

print(ask_ollama(prompt))