# project-c/Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY app/app.py .

RUN pip install flask
# Add prometheus_client
RUN pip install flask prometheus_client

EXPOSE 8080

CMD ["python", "app.py"]

