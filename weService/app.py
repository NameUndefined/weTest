#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,json,Response,make_response
#from database import *
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

@app.route('/')
def index():
    return 'hello'

@app.route('/titles/')
def titles():
    resp= make_response('''
    [    {
                'id':'1',
                'title':'十九大应知应会100题'
                },
                {
                'id':'2',
                'title':'政治常识100题'
                }
                ]
    ''',200)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp
    #t = Title.query().all()
    #return json.dumps({'titles':[title.to_json() for title in t]})
@app.route('/titles/<qid>/')
def questions(qid):
    qid=int(qid)
    if qid == 1 :
        resp= make_response('''
    [    {
                'id':'1',
                'qtype':'dx',
                'questiontext':'How much man likes woman?',
                'answer':'[1,2]',
                'chooses':'["1","10","dont know"]'
                },
                {
                'id':'2',
                'qtype':'pd',
                'questiontext':'do you like ck?',
                'answer':'[1]',
                'chooses':'[]'
                }
,
                {
                'id':'2',
                'qtype':'pd',
                'questiontext':'Are u crazy?',
                'answer':'[0]',
                'chooses':'[]'
                }
                ]
    ''',200)
    if qid == 2 :
        resp= make_response('''
    [    {
                'id':'1',
                'qtype':'dx',
                'questiontext':'Hou much you get a month?',
                'answer':'[1,2]',
                'chooses':'["10$","1000$","dont know","all"]'
                },
                {
                'id':'2',
                'qtype':'pd',
                'questiontext':'Are u CP?',
                'answer':'[1]',
                'chooses':'[]'
                }
,
                {
                'id':'2',
                'qtype':'pd',
                'questiontext':'Are u ok?',
                'answer':'[0]',
                'chooses':'[]'
                }
                ]
    ''',200)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp
    #q = Question.query().filter_by(id=qid).all()
    #return jsonify(q)
    #return 0
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


