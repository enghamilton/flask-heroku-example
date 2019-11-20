"""Flask App Project."""

import requests
from flask import Flask, jsonify
app = Flask(__name__)

USERNAME = "enghamilton"
#PASSWORD = "p4dcGj97"

LOGIN_URL = "https://github.com/login"
URL = "https://github.com/"

@app.route('/')
def index():
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
