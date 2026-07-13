package terraform.security

deny contains msg if {
    sg := input.resource.aws_security_group[_]
    rule := sg.ingress[_]

    rule.cidr_blocks[_] == "0.0.0.0/0"
    rule.from_port == 22

    msg := sprintf("Security Group '%s' should not allow SSH from 0.0.0.0/0.", [sg.name])
}