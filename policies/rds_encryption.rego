package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_db_instance"

    resource.change.after.storage_encrypted != true

    msg := sprintf("RDS '%s' should enable storage encryption.", [resource.name])
}