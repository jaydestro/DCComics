# Build your Python-based image
FROM python:3.9-slim-buster AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get -y install netcat gnupg gcc curl uwsgi-plugin-python3 && \
    apt-get clean

# Install MongoDB
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - && \
    echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list && \
    apt-get update && \
    apt-get -y install mongodb-org

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make /data/db for database
RUN mkdir -p /data/db

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Update CSV_DIRECTORY in config.py
RUN sed -i 's#CSV_DIRECTORY = "./data"#CSV_DIRECTORY = "/app/data"#g' config.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the MongoDB service and the Flask app in the background
CMD mongod --dbpath /data/db --bind_ip_all --fork --logpath  /var/log/mongodb.log && python app.py