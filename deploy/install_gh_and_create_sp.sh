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

# Create Service Principal
SP_NAME="DCComics$RANDOM_STRING"
echo "Creating Service Principal: $SP_NAME"
SP_JSON=$(az ad sp create-for-rbac --name "$SP_NAME" --role contributor --scopes /subscriptions/$SUBSCRIPTION_ID --sdk-auth)
CLIENT_ID=$(echo "$SP_JSON" | jq -r .clientId)
CLIENT_SECRET=$(echo "$SP_JSON" | jq -r .clientSecret)
TENANT_ID=$(echo "$SP_JSON" | jq -r .tenantId)

# Store Secrets in GitHub Repository
gh secret set AZURE_CLIENT_ID -b "$CLIENT_ID"
gh secret set AZURE_CLIENT_SECRET -b "$CLIENT_SECRET"
gh secret set AZURE_TENANT_ID -b "$TENANT_ID"
echo "Secrets stored in GitHub repository."

echo "Script completed."
