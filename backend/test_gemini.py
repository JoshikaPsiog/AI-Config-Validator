from ai.gemini_service import ask_gemini

prompt = """
Analyze this Terraform configuration issue:

S3 bucket allows public access.

Provide:
1. Problem
2. Security Risk
3. Recommended Fix
"""

print(ask_gemini(prompt))