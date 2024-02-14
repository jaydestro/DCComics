from flask import Flask, render_template, request
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from config import COSMOSDB_CONNECTION_STRING

app = Flask(__name__)

# Check if connection string is provided
if not COSMOSDB_CONNECTION_STRING:
    print("Error: No connection string provided. Please set the 'COSMOSDB_CONNECTION_STRING' in configuration.")
    exit()

# Azure Cosmos DB connection setup
try:
    client = CosmosClient.from_connection_string(COSMOSDB_CONNECTION_STRING)
    database_name = "DCComics"
    container_name = "ComicBooks"
    
    database = client.create_database_if_not_exists(id=database_name)
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/Issue_Link"),  # Use Issue_Link as the partition key
        offer_throughput=400
    )
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database=database_name)
    container = database.get_container_client(container_name)
except Exception as e:
    print(f"An error occurred while setting up Azure Cosmos DB connection: {e}")
    exit()

# Flask app route definitions
@app.route("/", methods=["GET", "POST"])
def index():
    # Fetch the total number of comics
    total_comics = container.query_items(
        query="SELECT VALUE COUNT(1) FROM c",
        enable_cross_partition_query=True
    ).next()

    # Query to get distinct Category_Title values, excluding null
    comic_series_query = "SELECT DISTINCT VALUE c.Comic_Series FROM c WHERE c.Comic_Series != null"
    comic_series = list(container.query_items(
        query=comic_series_query,
        enable_cross_partition_query=True
    ))

    if request.method == "POST":
        keyword = request.form.get("keyword")
        selected_series = request.form.get("series")

        # Start building the query and parameters
        search_query = "SELECT * FROM c WHERE "
        search_params = []
        conditions = []

        # Add condition for keyword if provided
        if keyword:
            conditions.append("CONTAINS(c.Issue_Name, @keyword, true)")
            search_params.append({"name": "@keyword", "value": keyword})

        # Add condition for selected series if provided and not 'All'
        if selected_series and selected_series != 'All':
            conditions.append("c.Comic_Series = @series")
            search_params.append({"name": "@series", "value": selected_series})

        # Combine conditions with 'AND' if any conditions are present
        if conditions:
            search_query += " AND ".join(conditions)
        else:
            # If no conditions, change query to select all items
            search_query = "SELECT * FROM c"

        # Execute the query
        comics = list(container.query_items(
            query=search_query,
            parameters=search_params,
            enable_cross_partition_query=True
        ))

        # Render the results template with the query results
        return render_template("results.html", comics=comics)

    # Render the index template with the list of comic series and total comic count
    return render_template("index.html", comic_series=comic_series, total_comics=total_comics)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
