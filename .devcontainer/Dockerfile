# Use the official Python 3 image as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the default command to run when the container starts
CMD [ "python", "app.py" ]