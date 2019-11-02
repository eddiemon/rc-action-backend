# app.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/v1/testing')
def testing():
    return json.dumps({"hej": "san"})

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
