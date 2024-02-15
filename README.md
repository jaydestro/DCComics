# DC Comics Comic Book Search Web App

This repository contains a simple web application built using Flask and Azure Cosmos DB that enables users to search for comic book information based on keywords.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Data Source](#data-source)
- [License](#license)

## Introduction

The DC Comics Comic Book Search Web App is designed to help users search for comic book information from an Azure Cosmos DB database using keyword-based queries. The web app uses Flask for the backend and provides a user-friendly interface for searching and displaying comic book details.

## Features

- Search for comic books based on keywords.
- Display search results in a table format.
- Supports case-insensitive search across multiple fields.

## Requirements

- Python 3.x
- Flask
- azure-cosmos
- An Azure Cosmos DB instance

## Components

### app.py

The main Flask application script that provides the user interface and handles user requests. It interacts with the Azure Cosmos DB database to fetch and display comic book data.

### config.py

Configuration file containing the Azure Cosmos DB connection string (`COSMOSDB_CONNECTION_STRING`) and other configuration parameters.

### import.py

A script to populate the Azure Cosmos DB database with comic book data from JSON files. It includes functions for validating and inserting data.

### Templates

- **index.html:** The template for the main search page, including forms for keyword search and browsing by comic series.

- **results.html:** The template for displaying search results in a tabular format, including details of matching comic books.

### Static

This directory contains static files like CSS stylesheets (`styles.css`) for styling the web pages.

## Installation

1. Fork this repository to your GitHub account and then clone it locally or open in a Codespace.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/jaydestro/DCComics)

```bash
git clone https://github.com/yourusername/DCComics
```

1. Navigate to the project directory:

```bash
cd dccomics
```

1. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

1. Before running the Data Importer (`import.py`), configure the Azure Cosmos DB connection details.

1. Open the `config.py` file in a text editor.

1. Update the Azure Cosmos DB connection string to match your Azure Cosmos DB setup. Modify the following line with your Azure Cosmos DB URI:

```python
COSMOSDB_CONNECTION_STRING = "your_connection_string_here"
```

> **Note:** You can sign up for a free Azure Cosmos DB account by going to [https://aka.ms/trycosmosdb](https://aka.ms/trycosmosdb). Start building with no credit card!

1. Save and close the `config.py` file.

1. Run the Data Importer to populate your Azure Cosmos DB database with comic book data:

```bash
python import.py
```

1. Run the Flask app:

```bash 
python app.py
```

The app will start running locally and you'll be able to access it in your web browser.

Open a web browser and navigate to http://127.0.0.1:5000/ to access the Comic Book Search Web App.

## Data Source

The comic book data used in this project is sourced from the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) available on Kaggle. This dataset provides comprehensive information about various DC comic books, including details about issues, creators, release dates, and more.

We are grateful to the creators of the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) for compiling and sharing this valuable collection of comic book information. The dataset forms the foundation of the comic book information available for search and exploration within the DC Comics Comic Book Search Web App.

Please visit the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) on Kaggle to learn more about the dataset, its structure, and the original contributors.

## License

This project is licensed under the [MIT License](LICENSE).
