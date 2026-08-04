package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_s3_bucket"

    resource.change.after.versioning.enabled != true

    msg := sprintf("S3 bucket '%s' should enable versioning.", [resource.name])
}