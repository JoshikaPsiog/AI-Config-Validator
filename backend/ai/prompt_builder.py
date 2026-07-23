def build_validation_prompt(validation_output: str):

    return f"""
You are an AWS Cloud Security Expert.

Analyze the following Conftest/Terraform validation result.

For every issue found, provide:

1. Reason for the failure.
2. Security impact.
3. Risk Level (Low / Medium / High).
4. Terraform recommendation to fix it.

Keep the explanation simple and professional.

Validation Output:

{validation_output}
"""