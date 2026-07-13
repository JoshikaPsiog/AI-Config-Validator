def get_recommendation(validation_results):

    recommendations = []

    for result in validation_results:

        if "Encryption Missing" in result:
            recommendations.append({
                "severity": "High",
                "issue": "Encryption Missing",
                "recommendation": "Enable server_side_encryption_configuration for your S3 bucket."
            })

        if "Resource Block Missing" in result:
            recommendations.append({
                "severity": "Medium",
                "issue": "Resource Block Missing",
                "recommendation": "Define at least one Terraform resource block."
            })

    return recommendations