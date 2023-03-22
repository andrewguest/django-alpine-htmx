import multiprocessing

# Gunicorn app
# Tell Gunicorn which application to run
wsgi_app = "django_examples.asgi:application"

# Requests
# Restart workers after so many requests, with some variability.
max_requests = 1000
max_requests_jitter = 50

# Logging
# Use stdout for logging
log_file = "-"

# Workers
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
