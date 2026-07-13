package terraform.region

allowed_regions := {
    "us-east-1",
    "us-west-2"
}

deny contains msg if {
    provider := input.provider.aws
    not allowed_regions[provider.region]

    msg := sprintf("Region '%s' is not allowed.", [provider.region])
}