# app.py
import flask
from flask import Flask, request, jsonify
from src.services.FCMservice import FCMService
import uuid
import os
from os import listdir
import subprocess

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
        tweets.append(f.read())
        f.close()

    return jsonify(tweets)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
