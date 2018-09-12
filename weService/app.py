#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, json, Response, make_response, request
from flask_sqlalchemy import SQLAlchemy
from database import *
import os, urllib

# app=Flask(__name__)


db.init_app(app)


# db.create_all()
@app.route('/')
def index():
    return 'Nice to meet u!'


@app.route('/pushrecord/<titleid>/<userIMEI>/<userScore>/<wrong>')
def pushrecord(titleid, userIMEI, userScore, wrong):
    record = Record(titleID=titleid, userIMEI=userIMEI, userScore=float(userScore), wrongQuestions=wrong)
    db.session.add(record)
    db.session.commit()
    resp = make_response('["status":"200"]')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/getrecord/<titleid>')
def getrecord(titleid):
    r = Record().query.filter_by(titleID=titleid).order_by(db.desc('userScore')).all()
    recordALL = [records.to_json() for records in r]
    for i in recordALL:
        imei = i['imei']
        user = User().query.filter_by(userIMEI=imei).all()[0]
        nick = user.userNick
        i['nick'] = nick
    resp = make_response(json.dumps(recordALL))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/user/<imei>/setnick/<nick>')
def setnick(imei, nick):
    # nick = urllib.unquote(nick)
    try:
        user = User().query.filter_by(userIMEI=imei).all()[0]
        user.userNick = nick
    except:
        user = User(userIMEI=imei, userNick=nick)
    db.session.add(user)
    db.session.commit()
    resp = make_response('["status":"200"]')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/titles/')
def titles():
    t = Title.query.order_by(db.desc('id')).limit(10).all()
    res = [title.to_json() for title in t]
    for i in res:
        id = i['id']
        times = len(Record().query.filter_by(titleID=id).all())
        i['times'] = times
    resp = make_response(json.dumps(res))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/titles/create', methods=['POST'])
def createtitle():
    astr = request.form['astr']
    title = request.form['title']
    newTitle = Title(title=title)
    db.session.add(newTitle)
    db.session.commit()
    title_id = newTitle.id
    t = astr.split(',')
    p = []
    for i in range(len(t)):
        if len(t[i]) > 1:
            p = '"'+t[i][0]+'"'
            for j in range(len(t[i]) - 1):
                p = p + ',"' + t[i][j + 1]+'"'
            t[i] = p
            print p
        if t[i] == 't': t[i] = 1
        if t[i] == 'f': t[i] = 0
    for i in t:
        if i == 0 or i == 1:
            q = Question(qtype='pd', title_id=title_id, questiontext=u'题目请看大屏幕', answer='[' + str(i) + ']',
                         chooses='[]')
        if i <> 0 and i <> 1:
            if len(i) == 1 :
                q = Question(qtype='dx', title_id=title_id, questiontext=u'题目请看大屏幕', answer='["' + i + '"]',
                         chooses='["A","B","C","D","E","F","G","H","I"]')
            if len(i) > 1:
                q = Question(qtype='dx2', title_id=title_id, questiontext=u'题目请看大屏幕', answer='[' + i + ']',
                         chooses='["A","B","C","D","E","F","G","H","I"]')
        db.session.add(q)
    db.session.commit()
    resp = make_response('ok')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/contests/')
def contests():
    t = Contest.query.all()
    c = []
    for i in t:
        c.append(Title.query.filter_by(id=i.titleid).all()[0])
    resp = make_response(json.dumps([contest.to_json() for contest in c]))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/contests/create/<titleid>/<timelimit>/')
def create_contests(titleid, timelimit):
    if len(Title.query.filter_by(id=titleid).all()) < 1:
        resp = make_response('["status":"404"]')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    t = Contest(titleid=titleid, timelimit=timelimit)
    db.session.add(t)
    db.session.commit()
    resp = make_response('["status":"200"]')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/articles/')
def articles():
    t = Article.query.all()
    resp = make_response(json.dumps([title.to_json() for title in t]))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/titles/<qid>/')
def questions(qid):
    qid = int(qid)
    t = Title.query.filter_by(id=qid).all()[0].questions
    resp = make_response(json.dumps([question.to_json() for question in t]))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8001)
