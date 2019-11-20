"""Flask App Project."""

import requests
from flask import Flask, jsonify
app = Flask(__name__)

USERNAME = "enghamilton"
PASSWORD = "*******7"

LOGIN_URL = "https://github.com/login"
URL = "https://github.com/"

@app.route('/')
def index():
    return "Hello World"

@app.route('/scraper')
def scraper():
    # Create payload
    payload = {
        "login": USERNAME, 
        "password": PASSWORD
    }

	#https ://pybit.es/requests-session.html
    with requests.Session() as session:
		post = session.post(LOGIN_URL, data=payload)
		r = session.get(URL)
    
    return "%s" % r.content


if __name__ == '__main__':
    app.run()
