import csv
from pymongo import MongoClient
import asyncio

async def insert_documents_async(collection, rows):
    """
    Inserts documents into the specified collection asynchronously.

    :param collection: The collection to insert documents into.
    :type collection: pymongo.collection.Collection
    :param rows: The rows to insert as documents.
    :type rows: list[dict]
    """
    tasks = []
    total_rows = len(rows)
    for i, row in enumerate(rows):
        tasks.append(asyncio.ensure_future(asyncio.to_thread(collection.insert_one, row)))
    await asyncio.gather(*tasks)

async def main():
    # Prompt user for Cosmos DB connection string
    connection_string = input("Please enter the Cosmos DB connection string: ")

    # Set up connection to Azure Cosmos DB for MongoDB
    client = MongoClient(connection_string)
    db = client['mydatabase']

    # Prompt user for database and collection name
    database_name = input("Please enter the name of the database: ")
    collection_name = input("Please enter the name of the collection: ")

    # Check if database exists, if not create it
    if database_name not in client.list_database_names():
        db = client[database_name]
        print("Database created.")
    else:
        db = client[database_name]

    # Check if collection exists, if not create it
    if collection_name not in db.list_collection_names():
        collection = db[collection_name]
        print("Collection created.")
    else:
        collection = db[collection_name]

    # Prompt user for CSV file location
    csv_file_location = input("Please enter the location of the CSV file: ")

    # Open CSV file and insert data into collection
    counter = 0
    rows = []
    with open(csv_file_location, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
            counter += 1
            print(f"{counter} documents read from CSV file.")

    print("Inserting documents into the collection...")
    await insert_documents_async(collection, rows)
    print("Documents inserted successfully.")

# Run the main function
asyncio.run(main())