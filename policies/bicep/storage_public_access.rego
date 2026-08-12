package main

deny contains msg if {
    resource := input.resources[_]

    resource.type == "Microsoft.Storage/storageAccounts"

    resource.properties.allowBlobPublicAccess == true

    msg := sprintf(
        "Storage Account '%s' should not allow public blob access.",
        [resource.name]
    )
}