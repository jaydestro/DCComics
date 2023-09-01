param location string = resourceGroup().location
param appServicePlanTier string = 'D1'
param appServicePlanInstances int = 1

var resourcePrefix = 'dccomics'
var resourceSuffix = 'dev'
var cosmosDbAccountName = '${resourcePrefix}-mongodb-${resourceSuffix}'
var websiteName = '${resourcePrefix}-web-${resourceSuffix}'
var hostingPlanName = '${resourcePrefix}-hosting-${resourceSuffix}'

resource cosmosDbAccount 'Microsoft.DocumentDB/databaseAccounts@2021-04-15' = {
  name: cosmosDbAccountName
  kind: 'MongoDB'
  location: location
  properties: {
    databaseAccountOfferType: 'Standard'
    locations: [
      {
        locationName: location
      }
    ]
  }
  tags: {
    deployment: 'development'
  }
}

resource hostingPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: hostingPlanName
  location: location
  tags: {
    deployment: 'development'
  }
  sku: {
    name: appServicePlanTier
    capacity: appServicePlanInstances
  }
  kind: 'Linux'
}

resource website 'Microsoft.Web/sites@2022-03-01' = {
  name: websiteName
  location: location
  tags: {
    deployment: 'development'
  }
  properties: {
    serverFarmId: hostingPlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'MONGODB_URI'
          value: cosmosDbAccount.properties.documentEndpoint
        }
      ]
    }
  }
}
