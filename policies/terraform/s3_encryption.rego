package terraform.security

deny contains msg if {
    resource := input.resource.aws_s3_bucket[_]
    not resource.server_side_encryption_configuration

    msg := sprintf("S3 bucket '%s' must have server-side encryption enabled.", [resource.name])
}