package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_instance"

    instance_type := resource.change.after.instance_type

    instance_type == "t2.micro"

    msg := sprintf("EC2 instance '%s' should not use t2.micro.", [resource.name])
}