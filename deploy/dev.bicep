param baseName string = 'dccomics'
param location string = 'eastus'

var random = uniqueString(baseName, 'abcd')

resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: 'appServicePlan-${random}'
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
  name: 'webApp-${random}'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
  }
  tags: {
    deployment: 'development'
  }
}

resource cosmosDbAccount 'Microsoft.DocumentDB/databaseAccounts@2021-04-15' = {
  name: 'cosmosdb-${random}'
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
  properties: {
    resource: {
      id: 'DCComics'
    }
  }
}

resource cosmosDbCollection 'Microsoft.DocumentDB/databaseAccounts/mongodbDatabases/collections@2021-04-15' = {
  parent: cosmosDbDatabase
  name: 'Comics'
  properties: {
    resource: {
      id: 'Comics'
    }
  }
}

output appServicePlanName string = appServicePlan.name
output appServiceName string = webApp.name
output cosmosDbAccountName string = cosmosDbAccount.name
