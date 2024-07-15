# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -U setuptools pyparsing docker python-iptables

# Expose the port that the application will run on
EXPOSE 8000

# Define the command to run the application
CMD ["python", "flaskApp.py"]