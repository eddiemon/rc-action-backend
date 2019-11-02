# app.py
from flask import Flask, request, jsonify
from src.services.FCMservice import FCMService
import uuid

app = Flask(__name__)

@app.route('/api/reportIncident', methods=['POST'])
def report_incident():
    event_id = generate_event_id()
    push_event_notification(event_id)
    return "", 200

def generate_event_id():
    return uuid.uuid4()

def push_event_notification(event_id):
    pass

@app.route('/api/testNotifications')
def test_push_notification():
    android_push_service = FCMService()
    android_push_service.send_push_notification("testmessage", ["", ""], low_priority=True)
    return "blah"

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
