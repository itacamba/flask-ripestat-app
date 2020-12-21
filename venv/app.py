from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import pprint
from validate_object import validate
from get_obj_data import get_data_for, who_is_data


app = Flask(__name__)
# db config
# app.config['SQLALCHEMY_DATABASE_URI'] = '<db-type>://<db-owner>:<server-password>@<server:host>/
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/ripe-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db
db = SQLAlchemy(app)



# inetnum model
class Inetnum(db.Model):
    __tablename__ = 'inetnums'
    id = db.Column(db.Integer(), primary_key=True)
    inetnum = db.Column(db.String(), unique=True, nullable=False)
    netname = db.Column(db.String(), nullable=False)
    org = db.Column(db.String())
    descr = db.Column(db.ARRAY(db.String()))
    country = db.Column(db.ARRAY(db.String()), nullable=False)
    status = db.Column(db.String(), nullable=False)
    mnt_by = db.Column(db.ARRAY(db.String()), nullable=False)
    mnt_lower = db.Column(db.ARRAY(db.String()))
    mnt_routes = db.Column(db.ARRAY(db.String()))
    created = db.Column(db.String(), nullable=False)
    last_modified = db.Column(db.String(), nullable=False)
    source = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Inetnum('{self.inetnum}', '{self.netname}', '{self.org}', '{self.descr}', '{self.country}', '{self.status}', '{self.mnt_by}', '{self.mnt_lower}', '{self.mnt_routes}', '{self.created}', '{self.last_modified}', '{self.source}')"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        obj = request.form['ripe_object']
        if validate(obj) == "inetnum":
            # data = get_data_for(obj, "inetnum")
            data = who_is_data(obj, "inetnum")
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