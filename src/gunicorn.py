
from src.settings import APP_DEFAULT_PORT, APP_DEFAULT_HOST

bind = f"{APP_DEFAULT_HOST}:{APP_DEFAULT_PORT}"
workers = 2
worker_class = "gevent"
worker_connections = 1000
max_requests = int(workers * worker_connections)
keepalive = 2
max_requests_jitter = 5
timeout = 30
