# pull official base image
FROM python:3.9.6-alpine

# Set the working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define the volumes to be mounted
VOLUME .:/app

# install dependencies
COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# Expose the required port
EXPOSE 8000

# Run the Django app
CMD bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"