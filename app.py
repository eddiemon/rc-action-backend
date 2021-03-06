# app.py
import flask
from flask import Flask, request, jsonify, url_for, send_from_directory
from src.services.FCMservice import FCMService
import uuid
import os
import json
from os import listdir
import subprocess

app = Flask(__name__)

unverified_events = []
verified_events = []


@app.route('/api/healthCheck', methods=['GET'])
def health_check():
    return "", 200



@app.route('/api/reportIncident', methods=['POST'])
def report_incident():
    event_id = generate_event_id()
    event_type = request.json.get("type")
    unverified_events.append(event_id)
    push_event_notification(event_id, event_type)
    return "", 200


def generate_event_id():
    return uuid.uuid4()


def push_event_notification(event_id, event_type):
    print("pushing notifications of event type " + event_type)
    pass


@app.route("/api/verifyEvent")
def verify_event():
    event_id = request.json.get("eventId")
    pass


@app.route('/api/testNotifications')
def test_push_notification():
    android_push_service = FCMService()
    android_push_service.send_push_notification("testmessage", ["", ""], low_priority=True)
    return "blah"


@app.route('/api/notification/response/<response_type>')
def notification_response_verification(response_type):
    if response_type == "verification":
        return "verification"
    elif response_type == "availability":
        return "availability"
    flask.abort(404)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/api/news')
def news():
    command = './run_script.sh'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, cwd="./tweet_scraper")
    process.wait()
    mypath = "./tweet_scraper/Data/tweet/"
    from os.path import isfile, join
    tweets = []
    
    for file in os.listdir(mypath):
        filepath = os.path.join(mypath, file)
        f = open(filepath, 'r')
        tweets.append(json.loads(f.read()))
        f.close()

    news = { "news": tweets }

    return jsonify(news)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'static/favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    PORT = 8000
    if os.getenv("PORT") is not None:
        PORT = os.getenv("PORT")
    app.run(threaded=True, port=PORT)
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
