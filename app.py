from flask import Flask, render_template, request
import re

from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB connection details
db = client["DCComics"]  # Use "DCComics" as the database name
collection = db["ComicBooks"]  # Use "ComicBooks" as the collection name

@app.route("/", methods=["GET", "POST"])
def index():
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
                {"Release_Date": re.compile(keyword, re.IGNORECASE)},
                {"Comic_Series": re.compile(keyword, re.IGNORECASE)},
                {"Comic_Type": re.compile(keyword, re.IGNORECASE)}
            ]
        })
        return render_template("results.html", comics=comics)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)