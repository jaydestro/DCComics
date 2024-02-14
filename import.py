from azure.cosmos import CosmosClient, exceptions, PartitionKey
import json
import jsonschema
from jsonschema import validate
import uuid
from datetime import datetime
import re
from tqdm import tqdm
import asyncio
import concurrent.futures
from config import COSMOSDB_CONNECTION_STRING, database_name, container_name, partition_key_path

# Function to create or get database
async def create_or_get_database(client, db_name):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, create_or_get_database_sync, client, db_name)

def create_or_get_database_sync(client, db_name):
    try:
        database = client.create_database_if_not_exists(db_name)
        print(f"Created database '{db_name}'")
    except exceptions.CosmosResourceExistsError:
        database = client.get_database_client(db_name)
        print(f"Database '{db_name}' already exists")
    return database

# Function to create or get container
async def create_or_get_container(database, cont_name, partition_key):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, create_or_get_container_sync, database, cont_name, partition_key)

def create_or_get_container_sync(database, cont_name, partition_key):
    try:
        container = database.create_container_if_not_exists(
            id=cont_name,
            partition_key=PartitionKey(path=partition_key)
        )
        print(f"Created container '{cont_name}'")
    except exceptions.CosmosResourceExistsError:
        container = database.get_container_client(cont_name)
        print(f"Container '{cont_name}' already exists")
    return container

# Function to validate and complete data based on the schema
async def validate_and_complete_data(data, schema):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, validate_and_complete_data_sync, data, schema)

def validate_and_complete_data_sync(data, schema):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as ve:
        print("Validation Error: ", ve)
        return False

    if 'id' not in data or not data['id']:
        data['id'] = str(uuid.uuid4())

    if 'Issue_Link' not in data or not data['Issue_Link']:
        print("Validation Error: 'Issue_Link' is required and must be unique.")
        return False

    # Here you can implement the uniqueness validation for Issue_Link if needed
    
    if 'Release_Date' in data:
        data['Release_Date'] = format_release_date(data['Release_Date'])
    return True

# Function to format the Release_Date
def format_release_date(date_str):
    month_year_pattern = re.compile(r"([a-zA-Z]+),\s*(\d{4})")
    try:
        month_year_match = month_year_pattern.match(date_str)
        if month_year_match:
            month, year = month_year_match.groups()
            formatted_date = datetime.strptime(f"{year} {month}", "%Y %B").strftime("%Y-%m-01")
            return formatted_date
        return date_str
    except ValueError:
        return date_str

# Define the JSON schema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "Category_Title": {"type": "string"},
        "Issue_Name": {"type": "string"},
        "Issue_Link": {"type": "string", "format": "uri"},
        "Pencilers": {"type": "string"},
        "Cover_Artists": {"type": "string"},
        "Inkers": {"type": "string"},
        "Writers": {"type": "string"},
        "Editors": {"type": "string"},
        "Executive_Editor": {"type": "string"},
        "Letterers": {"type": "string"},
        "Colourists": {"type": "string"},
        "Rating": {"type": "string"},
        "Release_Date": {"type": "string"},
        "Comic_Series": {"type": "string"},
        "Comic_Type": {"type": "string"},
        "id": {"type": "string"}
    },
    "required": ["Issue_Link"],
    "additionalProperties": False
}

# Main function to execute the script
async def main():
    # Initialize Cosmos DB client
    client = CosmosClient.from_connection_string(COSMOSDB_CONNECTION_STRING)

    # Create or get the database and container
    database = await create_or_get_database(client, database_name)
    container = await create_or_get_container(database, container_name, partition_key_path)

    # Load existing items from the container into memory
    existing_items = list(container.read_all_items())

    # Load existing "Issue_Link" values into a set for faster lookup
    existing_issue_links = {item["Issue_Link"] for item in existing_items}

    # Read JSON data from a file
    with open('data/Complete_DC_Comic_Books.json', 'r') as json_file:
        json_data = json.load(json_file)

    # Prepare and bulk insert data
    items_to_insert = []
    skipped_count = 0  # Initialize count for skipped documents

    print("Preparing and validating data...")
    for item in tqdm(json_data, desc="Processing Data"):
        if await validate_and_complete_data(item, schema):
            issue_link = item["Issue_Link"]
            # Check if the "Issue_Link" already exists
            if issue_link in existing_issue_links:
                skipped_count += 1
            else:
                items_to_insert.append(item)

    # Bulk insert operation with async
    print("Inserting Data...")
    with tqdm(total=len(items_to_insert) + skipped_count, desc="Inserting Data") as pbar:
        for item in items_to_insert:
            try:
                container.upsert_item(item)
                pbar.update(1)
            except exceptions.CosmosHttpResponseError as e:
                print(f"Failed to insert item {item['id']}: {e.message}")

    total_inserted = len(items_to_insert)
    total_count = total_inserted + skipped_count  # Include skipped documents in the total count

    print(f"Bulk insert operation completed. Total unique items inserted: {total_inserted}. Skipped items: {skipped_count}. Total count: {total_count}.")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
