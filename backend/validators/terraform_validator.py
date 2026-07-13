def validate_terraform(content: str):

    validation_result = []

    # Rule 1 - Resource Block
    if "resource" in content:
        validation_result.append("✅ Resource Block Found")
    else:
        validation_result.append("❌ Resource Block Missing")

    # Rule 2 - Encryption
    if "server_side_encryption_configuration" in content:
        validation_result.append("✅ Encryption Enabled")
    else:
        validation_result.append("❌ Encryption Missing")

    return validation_result