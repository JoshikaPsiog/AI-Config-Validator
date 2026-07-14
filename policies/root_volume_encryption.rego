package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_instance"

    resource.change.after.root_block_device[0].encrypted != true

    msg := sprintf(
        "Root volume for EC2 '%s' must be encrypted.",
        [resource.name]
    )
}