FROM python:3.12-slim-bullseye

# Set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Update the container OS
RUN apt update && apt upgrade -y

# Update pip
RUN python -m pip install --upgrade pip

# Copy the project's files into the container
RUN mkdir /code
WORKDIR /code

COPY . /code/

# Pip install requirements
RUN pip install -r requirements.txt

# Expose the container's port 8000
EXPOSE 8000

# Run the Django migrations
RUN python manage.py migrate

# Start the Django application
CMD ["gunicorn", "django_alpine_htmx.asgi:application"]
