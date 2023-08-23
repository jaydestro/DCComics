from flask import Flask, render_template, request
import re
from pymongo import MongoClient
from config import MONGODB_URI  # Import the connection string

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient(MONGODB_URI)  # Use the imported connection string
db = client["DCComics"]
collection = db["ComicBooks"]

# Create an index for Issue_Name field
collection.create_index([("Issue_Name", 1)])

@app.route("/", methods=["GET", "POST"])
def index():
    total_comics = collection.count_documents({})  # Total number of comic books

    # Retrieve unique comic series values for dropdown
    comic_series = collection.distinct("Comic_Series")

    if request.method == "POST":
        keyword = request.form.get("keyword")
        selected_series = request.form.get("series")  # Get selected comic series from dropdown
        
        # Construct the search query based on the selected series
        query = {
            "$or": [
                {"Issue_Name": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Issue_Link": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Pencilers": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Cover_Artists": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Inkers": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Writers": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Editors": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Executive_Editor": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Letterers": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Colourists": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Rating": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Comic_Series": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {},
                {"Comic_Type": re.compile(keyword, re.IGNORECASE)} if isinstance(keyword, str) else {}
            ]
        }
        if selected_series:  # Add series filter if a series is selected
            query["Comic_Series"] = selected_series
        
        comics = collection.find(query)
        return render_template("results.html", comics=comics, total_comics=total_comics)

    return render_template("index.html", comic_series=comic_series, total_comics=total_comics)

if __name__ == "__main__":
    app.run(debug=True)