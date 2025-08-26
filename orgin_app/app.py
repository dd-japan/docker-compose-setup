from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure Flask logger to use stdout
logging.basicConfig(level=logging.INFO)

@app.get("/health")
def health():
    app.logger.info("Health check called")
    return jsonify(status="ok")

@app.get("/")
def hello():
    app.logger.info("Root endpoint called")
    return "Hello from Flask in Docker on AL2023!"
