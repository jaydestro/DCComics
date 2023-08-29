# Azure AD Application and Service Principal Creation Script

Automate the creation of an Azure AD application, federated identity credential, and service principal for deploying a Bicep template to an Azure subscription. The script also sets the necessary secrets in the GitHub repository for authentication.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [Customization](#customization)
- [Disclaimer](#disclaimer)
- [License](#license)

## Prerequisites

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [GitHub CLI](https://cli.github.com/manual/installation)
- [jq (Command-line JSON Processor)](https://stedolan.github.io/jq/download/)

## Usage

1. Clone this repository to your local machine.

1. Open a terminal window and navigate to the repository directory.

1. Make the script executable if it's not already:

   ```bash
   chmod +x createsp.sh
   ```
1. Run the script:
   ```bash
   ./createsp.sh
   ```
1. **Follow the prompts and provide any required inputs when prompted.**

1. The script will create the necessary Azure AD application, federated identity credential, and service principal.

The script will also set the following secrets in your GitHub repository:

- `AZURE_CLIENT_ID`
- `AZURE_SUBSCRIPTION_ID`
- `AZURE_TENANT_ID`
- `RESOURCE_GROUP_NAME`

## Important Notes

- The script assumes that you are logged in to both Azure CLI and GitHub CLI with appropriate permissions.
- The generated secrets are sensitive information. Be careful not to expose them publicly.
- The `jq` tool is used in the script for processing JSON output.

## Customization

- You can modify the script to fit your specific requirements, such as changing the application name or modifying permissions.

## Disclaimer

This script is provided as-is and may require adjustments based on your environment and use case. Use it at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
