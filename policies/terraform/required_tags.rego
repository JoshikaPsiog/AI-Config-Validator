package terraform.tags

required_tags := {"Environment", "Owner"}

deny contains msg if {
    resource := input.resource.aws_instance[_]
    tag := required_tags[_]
    not resource.tags[tag]

    msg := sprintf("Resource '%s' is missing required tag '%s'.", [resource.name, tag])
}