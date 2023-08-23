# DC Comics Comic Book Search Web App

This repository contains a simple web application built using Flask and MongoDB that enables users to search for comic book information based on keywords.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Data Importer](#data-importer)
- [Data Source](#data-source)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
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


## Data Importer

If you have comic book data in a CSV format that you'd like to import into your MongoDB collection, we've provided a convenient data importer script in the `/data` directory. To get started with data import, follow the instructions in the [Data Importer README](./data/README.md).

As part of this repository, we have included a CSV file named `Complete_DC_Comic_Books.csv` containing comic book information. You can use this file to populate your MongoDB collection with sample data. To import this CSV data, follow the instructions provided in the [Data Importer README](./data/README.md).

The data importer script utilizes asynchronous programming techniques to efficiently import data from a CSV file into your MongoDB collection. It's a great way to populate your collection with comic book information for testing or demonstration purposes.

Feel free to explore the data importer's README for detailed steps on how to run the script and import the provided `Complete_DC_Comic_Books.csv` data into the MongoDB collection.

Once you've imported the data, you can use the Comic Book Search Web App to search and interact with the imported comic book information.

[Go to Data Importer README](./data/README.md)

## Data Source

The comic book data used in this project is sourced from the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) available on Kaggle. This dataset provides comprehensive information about various DC comic books, including details about issues, creators, release dates, and more.

We are grateful to the creators of the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) for compiling and sharing this valuable collection of comic book information. The dataset forms the foundation of the comic book information available for search and exploration within the DC Comics Comic Book Search Web App.

Please visit the [DC Comic Books Dataset](https://www.kaggle.com/datasets/deepcontractor/dc-comic-books-dataset) on Kaggle to learn more about the dataset, its structure, and the original contributors.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/jaydestro/DCComics
```

2. Install the required dependencies using pip:

```bash
pip install Flask pymongo Flask-static
```

3. Navigate to the project directory:

```bash
cd DCComics
```

## Configuration

Before running the Comic Book Search Web App, you need to configure the MongoDB connection details and ensure that your MongoDB collection contains documents with fields matching the specified schema.

1. Open the `config.py` file in a text editor.

2. Update the MongoDB connection details to match your MongoDB setup. Modify the following line with your MongoDB URI:

```bash 
MONGODB_URI = "mongodb://localhost:27017/" # Connection string for MongoDB server
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

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore, modify, and use this web app as a starting point for your own projects. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or pull request.

