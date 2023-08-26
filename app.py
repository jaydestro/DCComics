from flask import Flask, render_template, request
import re
from pymongo import MongoClient
from config import MONGODB_URI
import os
import asyncio
import csv

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient(MONGODB_URI)
db = client["DCComics"]
collection = db["ComicBooks"]

# Create an index for Issue_Name field
collection.create_index([("Issue_Name", 1)])

async def insert_documents_async(rows):
    tasks = []
    for row in rows:
        tasks.append(asyncio.ensure_future(asyncio.to_thread(collection.insert_one, row)))
    await asyncio.gather(*tasks)

def import_csv_from_directory(data_directory):
    total_comics_db = collection.count_documents({})
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
                    print(f"Importing data from {csv_file}...")
                    asyncio.run(insert_documents_async(rows))
                    print(f"{total_comics_csv} documents inserted from {csv_file}.")
                else:
                    print(f"No data imported from {csv_file} as the number of comics in the database and CSV match.")
            else:
                print(f"No data imported from {csv_file} as the number of comics in the database and CSV match.")

# Data import if the script is run directly
if __name__ == '__main__':
    import_csv_from_directory("data")  # Import CSV from the 'data' directory

# Flask app route definitions
@app.route("/", methods=["GET", "POST"])
def index():
    total_comics = collection.count_documents({})
    comic_series = collection.distinct("Comic_Series")

    if request.method == "POST":
        keyword = request.form.get("keyword")
        selected_series = request.form.get("series")

        query_conditions = []

        if isinstance(keyword, str) and keyword:
            compiled_keyword = re.compile(keyword, re.IGNORECASE)

            query_conditions.append({"Issue_Name": compiled_keyword})
            query_conditions.append({"Issue_Link": compiled_keyword})
            query_conditions.append({"Pencilers": compiled_keyword})
            query_conditions.append({"Cover_Artists": compiled_keyword})
            query_conditions.append({"Inkers": compiled_keyword})
            query_conditions.append({"Writers": compiled_keyword})
            query_conditions.append({"Editors": compiled_keyword})
            query_conditions.append({"Executive_Editor": compiled_keyword})
            query_conditions.append({"Letterers": compiled_keyword})
            query_conditions.append({"Colourists": compiled_keyword})
            query_conditions.append({"Rating": compiled_keyword})
            query_conditions.append({"Comic_Series": compiled_keyword})
            query_conditions.append({"Comic_Type": compiled_keyword})

        if selected_series:
            query_conditions.append({"Comic_Series": selected_series})

        query = {"$or": query_conditions}

        comics = collection.find(query)
        return render_template("results.html", comics=comics, total_comics=total_comics)

    return render_template("index.html", comic_series=comic_series, total_comics=total_comics)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')