#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,json,Response,make_response
from flask_sqlalchemy import SQLAlchemy
from database import *
import os
#app=Flask(__name__)


db.init_app(app)
#db.create_all()
@app.route('/')
def index():
    return 'Nice to meet u!'
@app.route('/pull')
def pull():
    os.chdir('c://zxdt-webroot/weTest')
    return os.system('git pull')
    #return 'hello'

@app.route('/titles/')
def titles():
    t = Title.query.all()
    resp= make_response(json.dumps([title.to_json() for title in t]))
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

@app.route('/titles/<qid>/')
def questions(qid):
    qid=int(qid)
    t = Title.query.filter_by(id=qid).all()[0].questions
    resp= make_response(json.dumps([question.to_json() for question in t]))
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')