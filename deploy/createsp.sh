#!/bin/bash

# Get the subscription ID using Azure CLI
SUBSCRIPTION_ID=$(az account show --query 'id' --output tsv)
echo "Subscription ID retrieved: $SUBSCRIPTION_ID"

# Set the subscription name using Azure CLI
SUBSCRIPTION_NAME=$(az account show --query 'name' --output tsv)
echo "Subscription Name: $SUBSCRIPTION_NAME"

# Check if jq is not installed and install it
if ! command -v jq &> /dev/null; then
    echo "Installing jq..."
    sudo apt-get update
    sudo apt-get install -y jq
    echo "jq installed."
fi

# Generate a random string
RANDOM_STRING=$(openssl rand -hex 5)

# Set federated identity

githubOrgAndRepo=$(gh repo view --json nameWithOwner -q ".nameWithOwner")
branchName='development'
applicationName="dccomics-$RANDOM_STRING"

# Create an Azure AD application
aksDeploymentApplicationDetails=$(az ad app create --display-name $applicationName)
aksDeploymentApplicationObjectId=$(echo $aksDeploymentApplicationDetails | jq -r '.id')
aksDeploymentApplicationAppId=$(echo $aksDeploymentApplicationDetails | jq -r '.appId')

# Create a federated identity credential for the application
az ad app federated-credential create \
   --id $aksDeploymentApplicationObjectId \
   --parameters "{\"name\":\"${applicationName}\",\"issuer\":\"https://token.actions.githubusercontent.com\",\"subject\":\"repo:${githubOrgAndRepo}:ref:refs/heads/${branchName}\",\"audiences\":[\"api://AzureADTokenExchange\"]}"

# Create a service principal for the application
az ad sp create --id $aksDeploymentApplicationObjectId

# Assign the application permissions to the subscription to deploy the Bicep template
az role assignment create \
   --assignee $aksDeploymentApplicationAppId \
   --role Owner \
   --scope "/subscriptions/${SUBSCRIPTION_ID}"

# Store Secrets in GitHub Repository
gh secret set AZURE_CLIENT_ID -b "$aksDeploymentApplicationAppId"
gh secret set AZURE_SUBSCRIPTION_ID -b "$SUBSCRIPTION_ID"
gh secret set AZURE_TENANT_ID -b "$(az account show --query tenantId --output tsv)" 

echo "Script completed."
