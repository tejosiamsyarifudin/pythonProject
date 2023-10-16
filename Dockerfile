# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# Set the working directory in the container
WORKDIR /

# Copy the requirements file into the container at /src
COPY requirements.txt /src/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /src
COPY . /src/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME fast-api-docker

# Set the maintainer label
LABEL maintainer="tejosiam <tejosiam@gmail.com>"

# Run main.py when the container launches
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]DockerfileCopy code