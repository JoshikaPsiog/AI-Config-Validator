def build_prompt(resource_name: str, issue: str):

    return f"""
You are an Infrastructure as Code security expert.

Resource:
{resource_name}

Detected Issue:
{issue}

Provide:

1. Explanation
2. Security Risk
3. Recommended Terraform Fix
4. Best Practice
"""