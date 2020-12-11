from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import pprint

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get('https://stat.ripe.net/data/whois/data.json?resource=185.83.156.0')
    data = r.json()['data']['records'][0]
    return render_template('ripe_object.html', data=data)

