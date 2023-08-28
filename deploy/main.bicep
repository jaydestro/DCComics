param baseName string = 'dccomics'
param location string = 'eastus'

param random string = uniqueString('abcd', utcNow())

param appName string = '${baseName}-${random}'
param appServicePlanName string = '${baseName}-plan-${random}'
param cosmosDbAccountName string = '${baseName}-db-${random}'
param cosmosDbDatabaseName string = 'DCComics'
param cosmosDbCollectionName string = 'Comics'

resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: 'F1'
    capacity: 1
  }
  tags: {
    deployment: 'production'
  }
}

resource webApp 'Microsoft.Web/sites@2020-06-01' = {
  name: appName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
  }
  tags: {
    deployment: 'production'
  }
}

resource cosmosDbAccount 'Microsoft.DocumentDB/databaseAccounts@2021-04-15' = {
  name: cosmosDbAccountName
  location: location
  kind: 'MongoDB'
  properties: {
    databaseAccountOfferType: 'Standard'
  }
  tags: {
    deployment: 'production'
  }
}

resource cosmosDbDatabase 'Microsoft.DocumentDB/databaseAccounts/mongodbDatabases@2021-04-15' = {
  parent: cosmosDbAccount
  name: cosmosDbDatabaseName
  properties: {
    resource: {
      id: cosmosDbDatabaseName
    }
  }
  tags: {
    deployment: 'production'
  }
}

resource cosmosDbCollection 'Microsoft.DocumentDB/databaseAccounts/mongodbDatabases/collections@2021-04-15' = {
  parent: cosmosDbDatabase
  name: cosmosDbCollectionName
  properties: {
    resource: {
      id: cosmosDbCollectionName
    }
  }
  tags: {
    deployment: 'production'
  }
}

output appServicePlanId string = appServicePlan.id
output appServiceName string = webApp.name
output cosmosDbConnectionString string = listKeys(cosmosDbAccount.id, '2021-04-15').connectionStrings[0].connectionString
