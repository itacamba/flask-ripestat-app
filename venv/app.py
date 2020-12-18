from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import pprint
from validate_object import validate
from get_obj_data import get_data_for


app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        obj = request.form['ripe_object']
        if validate(obj) == "inetnum":
            data = get_data_for(obj, "inetnum")
            return render_template('ripe_object.html', title="Inetnum", data=data, obj_type="inetnum")
        elif validate(obj) == "organisation":
            obj = get_data_for(obj)
            return render_template('ripe_object.html', title="Organisation", obj=obj, obj_type="organisation")
        else:
            return "no match"
    else:
        return render_template('home.html', title='Home Page')


@app.route('/<obj>')
def ripe_object(obj):
    return render_template('ripe_object.html', obj=obj, title="Ripe Object")
    # return render_template('ripe_object.html', title="Ripe Object", obj=obj)