# Use an image with Python 3.10 or higher
FROM python:3.10

# Set the working directory
WORKDIR /FictionalBandWebPage

# Copy the project files into the container
COPY . /FictionalBandWebPage

# Copy requirements.txt to the root of the Django project
COPY requirements.txt /FictionalBandWebPage/requirements.txt

# Update pip to the latest version and install project dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Define the command to run your application
CMD ["python", "website/manage.py", "runserver", "0.0.0.0:8000"]
