package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_ebs_volume"

    resource.change.after.encrypted != true

    msg := sprintf(
        "EBS volume '%s' must have encryption enabled.",
        [resource.name]
    )
}