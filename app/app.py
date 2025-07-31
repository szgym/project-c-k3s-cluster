from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Define metrics
http_requests_total = Counter('http_requests_total', 'Total HTTP requests')
index_requests_total = Counter('index_requests_total', 'Index page requests')

@app.route('/')
def index():
    http_requests_total.inc()
    index_requests_total.inc()
    return "Hello from k3s + Helm!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

