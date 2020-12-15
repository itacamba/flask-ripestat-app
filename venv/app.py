from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import pprint


app = Flask(__name__)

# @app.route('/')
# def index():
#     r = requests.get('https://stat.ripe.net/data/whois/data.json?resource=185.83.156.0')
#     data = r.json()['data']['records'][0]
#     return render_template('ripe_object.html', data=data)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        obj = request.form['ripe_object']
        if re.match(r'^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$', obj):
            return redirect(url_for('ripe_object', obj=obj))
        else:
            return "no match"
    else:
        return render_template('home.html', title='Home Page')


@app.route('/<obj>')
def ripe_object(obj):
    return render_template('ripe_object.html', obj=obj, title="Ripe Object")
    # return render_template('ripe_object.html', title="Ripe Object", obj=obj)