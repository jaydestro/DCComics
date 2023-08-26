import csv
from pymongo import MongoClient
import asyncio
import argparse

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
        # Check if document already exists in the collection
        if collection.find_one(row):
            print(f"Skipping document {i+1} as it already exists in the collection.")
            continue
        tasks.append(asyncio.ensure_future(asyncio.to_thread(collection.insert_one, row)))
    await asyncio.gather(*tasks)

async def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Import data from a CSV file into a MongoDB collection.')
    parser.add_argument('--connection-string', required=False, help='The Cosmos DB connection string.')
    parser.add_argument('--database-name', required=False, help='The name of the database.')
    parser.add_argument('--collection-name', required=False, help='The name of the collection.')
    parser.add_argument('--csv-file-location', required=False, help='The location of the CSV file.')
    args = parser.parse_args()

    # Prompt user for arguments if not provided
    if not args.connection_string:
        args.connection_string = input("Enter the Cosmos DB connection string: ")
    if not args.database_name:
        args.database_name = input("Enter the name of the database: ")
    if not args.collection_name:
        args.collection_name = input("Enter the name of the collection: ")
    if not args.csv_file_location:
        args.csv_file_location = input("Enter the location of the CSV file: ")

    # Set up connection to Azure Cosmos DB for MongoDB
    client = MongoClient(args.connection_string)
    db = client[args.database_name]

    # Check if database exists, if not create it
    if args.database_name not in client.list_database_names():
        db = client[args.database_name]
        print("Database created.")
    else:
        db = client[args.database_name]

    # Check if collection exists, if not create it
    if args.collection_name not in db.list_collection_names():
        collection = db[args.collection_name]
        print("Collection created.")
    else:
        collection = db[args.collection_name]

    # Open CSV file and insert data into collection
    counter = 0
    rows = []
    with open(args.csv_file_location, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
            counter += 1
            print(f"{counter} documents read from CSV file.")

    print("Inserting documents into the collection...")
    await insert_documents_async(collection, rows)
    print(f"{len(rows)} documents inserted successfully.")

# Run the main function
asyncio.run(main())