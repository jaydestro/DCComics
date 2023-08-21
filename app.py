from flask import Flask, render_template, request
import re
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["DCComics"]
collection = db["ComicBooks"]

# Create an index for Issue_Name field
collection.create_index([("Issue_Name", 1)])

@app.route("/", methods=["GET", "POST"])
def index():
    total_comics = collection.count_documents({})  # Total number of comic books

    if request.method == "POST":
        keyword = request.form.get("keyword")
        comics = collection.find({
            "$or": [
                {"Issue_Name": re.compile(keyword, re.IGNORECASE)},
                {"Issue_Link": re.compile(keyword, re.IGNORECASE)},
                {"Pencilers": re.compile(keyword, re.IGNORECASE)},
                {"Cover_Artists": re.compile(keyword, re.IGNORECASE)},
                {"Inkers": re.compile(keyword, re.IGNORECASE)},
                {"Writers": re.compile(keyword, re.IGNORECASE)},
                {"Editors": re.compile(keyword, re.IGNORECASE)},
                {"Executive_Editor": re.compile(keyword, re.IGNORECASE)},
                {"Letterers": re.compile(keyword, re.IGNORECASE)},
                {"Colourists": re.compile(keyword, re.IGNORECASE)},
                {"Rating": re.compile(keyword, re.IGNORECASE)},
                {"Comic_Series": re.compile(keyword, re.IGNORECASE)},
                {"Comic_Type": re.compile(keyword, re.IGNORECASE)}
            ]
        })
        return render_template("results.html", comics=comics, total_comics=total_comics)

    return render_template("index.html", total_comics=total_comics)

if __name__ == "__main__":
    app.run(debug=True)
