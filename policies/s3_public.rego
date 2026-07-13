package main

deny contains msg if {
    some bucket_name

    bucket := input.resource.aws_s3_bucket[bucket_name][_]

    bucket.acl == "public-read"

    msg := sprintf("S3 Bucket '%s' should not be public.", [bucket_name])
}