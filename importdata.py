from pymongo import MongoClient
import asyncio
import csv
import os
from config import MONGODB_URI  # Import the connection string

# MongoDB connection setup
client = MongoClient(MONGODB_URI)  # Use the imported connection string
db = client["DCComics"]
collection = db["ComicBooks"]

# Create an index for Issue_Name field
collection.create_index([("Issue_Name", 1)])

async def insert_documents_async(rows):
    """
    Inserts documents into the collection asynchronously.

    :param rows: The rows to insert as documents.
    :type rows: list[dict]
    """
    tasks = []
    for row in rows:
        tasks.append(asyncio.ensure_future(asyncio.to_thread(collection.insert_one, row)))
    await asyncio.gather(*tasks)

def import_csv_from_directory(data_directory):
    total_comics_db = collection.count_documents({})  # Total number of comic books in the database
    print(f"Total comics in database: {total_comics_db}")

    csv_files = [f for f in os.listdir(data_directory) if f.endswith(".csv")]

    if csv_files:
        for csv_file in csv_files:
            csv_file_location = os.path.join(data_directory, csv_file)
            rows = []
            with open(csv_file_location, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    rows.append(row)

            if rows:
                total_comics_csv = len(rows)
                print(f"Total comics in CSV {csv_file}: {total_comics_csv}")
                if total_comics_db != total_comics_csv:
                    # Check if the data is actually being compared and imported
                    print(f"Importing data from {csv_file}...")
                    asyncio.run(insert_documents_async(rows))
                    print(f"{total_comics_csv} documents inserted from {csv_file}.")
                else:
                    print(f"No data imported from {csv_file} as the number of comics in the database and CSV match.")
            else:
                print(f"No data imported from {csv_file} as the number of comics in the database and CSV match.")

if __name__ == '__main__':
    import_csv_from_directory("data")  # Import CSV from the 'data' directory