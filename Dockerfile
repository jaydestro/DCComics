# Use an official Python runtime as a parent image
FROM python:3.9.1-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install MongoDB from official repository
RUN apt-get update && \
    apt-get install -y gnupg curl && \
    curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - && \
    echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list && \
    apt-get update && \
    apt-get install -y mongodb-org

# Copy the current directory contents into the container at /app
COPY . /app

# Make /data/db for database
RUN mkdir -p /data/db

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Expose port 27017 for the MongoDB Server
EXPOSE 27017

# Start MongoDB service and initialize the database
RUN mongod --bind_ip_all --dbpath /data/db --fork --logpath /var/log/mongodb.log && sleep 5 && \
python ./data/importdata.py --connection-string "mongodb://127.0.0.1:27017/" --database-name "DCComics" --collection-name "Comics" --csv-file-location "./data/Complete_DC_Comic_Books.csv" && mongod --dbpath /data/db --shutdown 

# Run the Flask app in the background
CMD mongod --dbpath /data/db --bind_ip_all --fork --logpath  /var/log/mongodb.log && python ./app.py 