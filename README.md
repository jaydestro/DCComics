# DC Comics Comic Book Search Web App

This repository contains a simple web application built using Flask and MongoDB that enables users to search for comic book information based on keywords.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Data Importer](#data-importer-cli)
- [Data Source](#data-source)
- [License](#license)

## Introduction

The DC Comics Comic Book Search Web App is designed to help users search for comic book information from a MongoDB database using keyword-based queries. The web app uses Flask for the backend and provides a user-friendly interface for searching and displaying comic book details.

## Features

- Search for comic books based on keywords.
- Display search results in a table format.
- Supports case-insensitive search across multiple fields.

## Requirements

- Python 3.x
- Flask
- pymongo
- A MongoDB server

## Components

### app.py

The main Flask application script that provides the user interface and handles user requests. It interacts with the MongoDB database to fetch and display comic book data.

### config.py

Configuration file containing the MongoDB connection string (`MONGODB_URI`) and the CSV data directory path (`CSV_DIRECTORY`).

### importdata.py

A script to populate the MongoDB database with comic book data from CSV files. It includes functions for asynchronous insertion of data.

### Templates

- **index.html:** The template for the main search page, including forms for keyword search and browsing by comic series.

- **results.html:** The template for displaying search results in a tabular format, including details of matching comic books.

### Static

This directory contains static files like CSS stylesheets (`styles.css`) for styling the web pages.

## Installation

1. Fork this repository to your GitHub account and then clone it locally.

```bash
git clone https://github.com/yourusername/DCComics
```
2. Navigate to the project directory:

```bash
cd dccomics
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the Comic Book Search Web App, you need to configure the MongoDB connection details and ensure that your MongoDB collection contains documents with fields matching the specified schema.

1. Open the `config.py` file in a text editor.

2. Update the MongoDB connection details to match your MongoDB setup. Modify the following line with your MongoDB URI:

```bash
MONGODB_URI = "mongodb://localhost:27017/" # Connection string for MongoDB server
CSV_DIRECTORY = "./data"  # Path to the directory containing CSV files
```

> **Note:** If you have a remote MongoDB server, replace the connection string in the code with the appropriate connection string for your server.
>

### Get Started with Azure Cosmos DB for MongoDB

You can sign up for Azure Cosmos DB for MongoDB for free and start building scalable applications. To get started, visit [https://aka.ms/trycosmosdb](https://aka.ms/trycosmosdb) to create a free account and explore the powerful features of Azure Cosmos DB.

3. Save and close the `app.py` file.

4. Run the Flask app:

```bash 
python app.py
```

The app will start running locally and you'll be able to access it in your web browser.

Open a web browser and navigate to http://127.0.0.1:5000/ to access the Comic Book Search Web App.

Use the search form to search for comic books based on keywords or browse by comic series. The results will be displayed in a table format.

To stop the Flask app, press **Ctrl+C** in the terminal where the app is running.

Remember to have a MongoDB server running and populated with comic book data for the app to work as expected.

## Usage

1. After following the installation steps mentioned in the previous section, you can access the DC Comics Comic Book Search Web App in your web browser by navigating to **http://127.0.0.1:5000/**.

2. The home page of the web app provides two main options for interacting with the comic book data:

   - **Keyword Search:** Enter a keyword related to the comic book you want to search for in the input field. Click the "Search" button to initiate the search. The search results will be displayed in a table format, showing various details of the matching comic books.

   - **Browse by Comic Series:** Use the dropdown menu to select a specific comic series. Click the "Browse" button to see all comic books from the selected series. The results will be displayed in a table format, similar to the keyword search.

3. For both the keyword search and browsing options, the search results table presents detailed information about the comic books. The columns include attributes such as issue name, pencilers, cover artists, writers, editors, release date, comic series, and more.

4. To search for another keyword or explore different comic series, you can return to the home page by clicking the "Search for another keyword" link.

5. Once you're done using the web app, you can stop the Flask app by pressing **Ctrl+C** in the terminal where the app is running.

Please note that the web app relies on the comic book data stored in your MongoDB collection. Ensure that your MongoDB server is running and contains the necessary comic book documents before using the search functionality.

Feel free to explore, modify, and use this web app as a starting point for your own projects. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or pull request.

## Data Importer CLI

As an example, we've provided a data importer CLI tool (`data_import_cli.py`) in the `/data` directory. This tool demonstrates how to populate a MongoDB collection with comic book data from a CSV file. However, please note that this importer is just an example and is not required to run the main web application. The web app itself can work with an existing MongoDB collection, and you can manually insert data or use your preferred method for data population.

The `data_import_cli.py` CLI tool showcases asynchronous programming techniques to efficiently import data from a CSV file into a MongoDB collection. It can be a helpful reference if you need to automate data import in a similar scenario.

As part of this repository, we have included a CSV file named `Complete_DC_Comic_Books.csv` containing comic book information. If you wish to use the example importer, follow the instructions in the [Data Importer README](./data/README.md).

> **Note:** Please remember that the data importer CLI tool is provided as an illustrative tool and is not necessary to run the main Comic Book Search Web App.

Feel free to explore the data importer's README for detailed steps on how to run the CLI tool and import the provided `Complete_DC_Comic_Books.csv` data into a MongoDB collection.

[Go to Data Importer README](./data/README.md)

## Data Source

The comic book data used in this project is sourced from the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) available on Kaggle. This dataset provides comprehensive information about various DC comic books, including details about issues, creators, release dates, and more.

We are grateful to the creators of the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) for compiling and sharing this valuable collection of comic book information. The dataset forms the foundation of the comic book information available for search and exploration within the DC Comics Comic Book Search Web App.

Please visit the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) on Kaggle to learn more about the dataset, its structure, and the original contributors.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore, modify, and use this web app as a starting point for your own projects. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or pull request.

