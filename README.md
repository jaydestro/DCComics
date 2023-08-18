# Comic Book Search Web App

This repository contains a simple web application built using Flask and MongoDB that enables users to search for comic book information based on keywords.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction

The Comic Book Search Web App is designed to help users search for comic book information from a MongoDB database using keyword-based queries. The web app uses Flask for the backend and provides a user-friendly interface for searching and displaying comic book details.

## Features

- Search for comic books based on keywords.
- Display search results in a table format.
- Supports case-insensitive search across multiple fields.

## Requirements

- Python 3.x
- Flask
- pymongo

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/comic-book-search.git
```

2. Install the required dependencies using pip:

```bash
pip install Flask pymongo
```

3. Navigate to the project directory:

```bash
cd comic-book-search
```

## Configuration

Before running the Comic Book Search Web App, you need to configure the MongoDB connection details and ensure that your MongoDB collection contains documents with fields matching the specified schema.

1. Open the `app.py` file in a text editor.

2. Update the MongoDB connection details to match your MongoDB setup. Modify the following line with your MongoDB URI:

```bash 
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection details
```

3. Save and close the `app.py` file.

4. Run the Flask app:

```bash 
python app.py
```

## Usage

1. Open a web browser and navigate to **http://127.0.0.1:5000/**.

1. Enter a keyword related to the comic book you want to search for in the input field.

1. Click the "Search" button to initiate the search.

1. The search results will be displayed in a table format, showing various details of the matching comic books.

1. To search for another keyword, click the "Search for another keyword" link.

1. To stop the Flask app, press **Ctrl+C** in the terminal where the app is running.
 
**Note:** Make sure your MongoDB collection contains documents with fields matching the specified schema.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore, modify, and use this web app as a starting point for your own projects. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or pull request.

