# Async MongoDB Data Import

This repository contains a Python script that demonstrates asynchronous data import from a CSV file into a MongoDB collection using the `pymongo` library and `asyncio` for managing asynchronous operations.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Data Source](#data-source)
- [License](#license)

## Introduction

The `importdata.py` script in this repository provides an example of how to efficiently import data from a CSV file into a MongoDB collection using asynchronous programming techniques. The script utilizes the `pymongo` library for interacting with MongoDB and `asyncio` for managing asynchronous tasks.

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
cd data
```

Run the script:

### Interactive Mode

Run the script interactively:

```bash
python importdata.py
```

### Command-Line Mode

Alternatively, you can use command-line flags to provide the necessary information:

```bash
python importdata.py --connection-string "your-connection-string" --database-name "your-database-name" --collection-name "your-collection-name" --csv-file-location "path-to-your-csv-file"
```

Follow the prompts to provide the MongoDB connection string, database and collection names, and the CSV file location. The script will read the CSV data and asynchronously insert it into the specified MongoDB collection.

## Data Source

The comic book data used in this project is sourced from the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) available on Kaggle. This dataset provides comprehensive information about various DC comic books, including details about issues, creators, release dates, and more.

We are grateful to the creators of the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) for compiling and sharing this valuable collection of comic book information. The dataset forms the foundation of the comic book information available for search and exploration within the DC Comics Comic Book Search Web App.

Please visit the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) on Kaggle to learn more about the dataset, its structure, and the original contributors.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to fork this repository, make modifications, and use it as a reference for your own projects involving asynchronous data import into MongoDB. If you find any issues or have suggestions for improvements, please open an issue or pull request.