# project-c/app/app.py
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from k3s + Helm!"

@app.route('/metrics')
def metrics():
    metric = 'demo_app_custom_metric 1\n'
    return Response(metric, mimetype='text/plain')

@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

