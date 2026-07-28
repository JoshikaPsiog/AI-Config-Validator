def build_validation_prompt(terraform_code):

    return f"""
You are a Terraform expert.

Analyze the following Terraform code and identify security issues.

Terraform Code:
{terraform_code}

Explain:
1. Security issues
2. Why they are risky
3. Recommended fixes
"""


def build_security_prompt(reason):

    return f"""
You are a Senior DevSecOps Engineer.

Analyze the following Conftest policy violation.

Violation:
{reason}

Respond ONLY in this format:

## Issue
Explain the problem.

## Risk
Explain why it is risky.

## Recommended Terraform Fix
Explain how to fix it.

Keep the response under 150 words.
"""