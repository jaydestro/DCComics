# Azure Service Principal Creation Script

Welcome to the **Azure Service Principal Creation Script** documentation! This script automates the process of creating a service principal in Azure, retrieving its credentials, and storing them as secrets in a GitHub repository. In this case, the script is specifically designed to prepare GitHub Actions with your Azure credentials, enabling you to automate resource creation and management.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Running the Script](#running-the-script)
- [Contributing](#contributing)
- [License](#license)


## Introduction

The `createsp.sh` script simplifies the creation of an Azure service principal, which is commonly used for automating tasks and granting controlled access to resources. This script streamlines the process and securely stores the resulting credentials as GitHub repository secrets. By preparing GitHub Actions with your Azure credentials, you can seamlessly automate the provisioning and management of Azure resources.

> **Note:** Please note that this script is provided for demonstration purposes and comes with no warranty. It's important to thoroughly review and understand the actions of the script before running it in a production environment.

## Usage

### Prerequisites

Before using the `createsp.sh` script, make sure you have the following prerequisites:

1. [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
2. [GitHub CLI](https://cli.github.com/manual/installation)

### Running the Script

1. Open a terminal window.

1. Make the script executable:

   ```bash
   chmod +x createsp.sh
   ```

1. Run the script:

   ```bash
   chmod +x createsp.sh
   ```

The script will guide you through the process of creating a service principal in Azure and storing its credentials as GitHub secrets.

Once the script completes, you'll find the following secrets in your GitHub repository:

- `AZURE_CLIENT_ID`: Azure service principal's client ID.
- `AZURE_CLIENT_SECRET`: Azure service principal's client secret.
- `AZURE_TENANT_ID`: Azure tenant ID.

## Contributing

If you'd like to contribute to this script, please follow these steps:

1. Fork the repository.

1. Create a new branch for your feature or bug fix: `git checkout -b feature/awesome-feature`

1. Make your changes and test thoroughly.

1. Commit your changes: `git commit -m "Add some feature"`

1. Push to the branch: `git push origin feature/awesome-feature`

1. Open a pull request!

## License

This script is licensed under the [MIT License](LICENSE).
