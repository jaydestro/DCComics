# Async MongoDB Data Import

This repository contains a Python script that demonstrates asynchronous data import from a CSV file into a MongoDB collection using the `pymongo` library and `asyncio` for managing asynchronous operations.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction

The `async_mongodb_data_import.py` script in this repository provides an example of how to efficiently import data from a CSV file into a MongoDB collection using asynchronous programming techniques. The script utilizes the `pymongo` library for interacting with MongoDB and `asyncio` for managing asynchronous tasks.

## Requirements

To run the script, you need:

- Python 3.x
- The `pymongo` library
- Basic understanding of MongoDB and asyncio

## Usage

Clone this repository to your local machine:

```bash
git clone git@github.com:jaydestro/DCComics.git
```

Install the required dependencies using `pip`:

```bash
pip install pymongo

```

Navigate to the repository directory:

```bash
cd async-mongodb-data-import
```

Run the script:

```bash
python async_mongodb_data_import.py
```

Follow the prompts to provide the Cosmos DB connection string, database and collection names, and the CSV file location. The script will read the CSV data and asynchronously insert it into the specified MongoDB collection.

## Configuration

- Modify the `async_mongodb_data_import.py` script if you need to customize the behavior or adapt it to your specific use case.
- Ensure that you have a valid Azure Cosmos DB connection string and MongoDB-compatible setup before running the script.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to fork this repository, make modifications, and use it as a reference for your own projects involving asynchronous data import into MongoDB. If you find any issues or have suggestions for improvements, please open an issue or pull request.