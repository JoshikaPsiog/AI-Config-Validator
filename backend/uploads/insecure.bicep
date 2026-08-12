resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'demostorage123'
  location: resourceGroup().location

  sku: {
    name: 'Standard_LRS'
  }

  kind: 'StorageV2'

  properties: {
    allowBlobPublicAccess: true
  }
}
