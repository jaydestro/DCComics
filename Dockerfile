# Use an official Python runtime as a parent image
FROM python:3.9.1-slim-buster as python-base

# Set the working directory to /app
WORKDIR /app

# Install MongoDB from official repository
RUN apt-get update && \
    apt-get install -y gnupg gcc curl && \
    curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - && \
    echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list && \
    apt-get update && \
    apt-get install -y mongodb-org

# Copy the current directory contents into the container at /app
COPY . /app

# Make /data/db for database
RUN mkdir -p /data/db

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

FROM python-base as app-image
# Expose port 5000 for the Flask app
EXPOSE 5000

# Start MongoDB service and initialize the database
RUN mongod --bind_ip_all --dbpath /data/db --fork --logpath /var/log/mongodb.log && sleep 5 && python ./data/importdata.py --connection-string "mongodb://127.0.0.1:27017/" --database-name "DCComics" --collection-name "ComicBooks" --csv-file-location "./data/Complete_DC_Comic_Books.csv" && mongod --dbpath /data/db --shutdown 

# Run the MongoDB service and the Flask app in the background
CMD mongod --dbpath /data/db --bind_ip_all --fork --logpath  /var/log/mongodb.log && uwsgi --http-socket :5000  --plugin python --wsgi-file /app/app.py --callable app --pythonpath /usr/local/bin/python3