## Use the official Python image as the base image
FROM python:3.11.5

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy your Django project code to the container
COPY . /app/

# Install Django project dependencies
RUN pip install -r requirements.txt

# Expose the port your Django app will run on
EXPOSE 8000

# Command to start your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
