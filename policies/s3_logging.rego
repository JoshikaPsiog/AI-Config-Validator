package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_s3_bucket"

    not resource.change.after.logging

    msg := sprintf(
        "S3 bucket '%s' should have access logging enabled.",
        [resource.name]
    )
}