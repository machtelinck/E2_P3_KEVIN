# pull official base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Install system dependencies
# RUN apk add --no-cache build-base

# # Install required libraries for numpy
# RUN apk add --no-cache openblas-dev libffi-dev

# Define the volumes to be mounted
VOLUME .:/app

# install dependencies
COPY ./requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# Expose the required port
EXPOSE 8000

# Run the Django app
CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"