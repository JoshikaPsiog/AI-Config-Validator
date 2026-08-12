from pathlib import Path
from services.bicep_validator import validate_bicep

# Project root (AI-Config-Validator)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Full path to the Bicep file
BICEP_FILE = PROJECT_ROOT / "uploads" / "insecure.bicep"

result = validate_bicep(
    str(BICEP_FILE),
    str(PROJECT_ROOT)
)

print(result)