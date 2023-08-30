param baseName string = 'dccomics'
param location string = 'eastus'

var uniqueNameComponent = uniqueString(resourceGroup().id)

resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: 'appServicePlan-${uniqueNameComponent}'
  location: location
  sku: {
    name: 'F1'
    capacity: 1
  }
  tags: {
    deployment: 'development'
  }
}

resource webApp 'Microsoft.Web/sites@2020-06-01' = {
  name: 'webApp-${uniqueNameComponent}'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
  }
  tags: {
    deployment: 'development'
  }
}

resource cosmosDbAccount 'Microsoft.DocumentDB/databaseAccounts@2021-04-15' = {
  name: 'cosmosdb-${uniqueNameComponent}'
  location: location
  kind: 'MongoDB'
  properties: {
    databaseAccountOfferType: 'Standard'
  }
  tags: {
    deployment: 'development'
  }
}

resource cosmosDbDatabase 'Microsoft.DocumentDB/databaseAccounts/mongodbDatabases@2021-04-15' = {
  parent: cosmosDbAccount
  name: 'DCComics'
}

resource cosmosDbCollection 'Microsoft.DocumentDB/databaseAccounts/mongodbDatabases/collections@2021-04-15' = {
  parent: cosmosDbDatabase
  name: 'Comics'
}

output appServicePlanName string = appServicePlan.name
output appServiceName string = webApp.name
output cosmosDbAccountName string = cosmosDbAccount.name
