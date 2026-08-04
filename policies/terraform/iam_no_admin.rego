package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_iam_policy"

    contains(resource.change.after.policy, "*")

    msg := "IAM policy should not allow full admin access."
}