package policies

deny contains msg if {
    resource := input.resource_changes[_]
    resource.type == "aws_db_instance"

    resource.change.after.backup_retention_period == 0

    msg := sprintf("RDS '%s' should have backups enabled.", [resource.name])
}