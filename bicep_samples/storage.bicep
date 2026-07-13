resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'demostorage12345'
  location: resourceGroup().location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}