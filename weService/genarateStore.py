#!/usr/bin/env python
# -*- coding: utf-8 -*-
from database import db,Question,Title
import sys,os,json

f = file('store.txt')
f.seek(0)
title = f.readline().decode('utf-8')
newTitle = Title(title=title)
db.session.add(newTitle)
db.session.commit()
title_id = newTitle.id
while True :
    tmp = f.readline()
    tmp =tmp.decode('utf-8')
    QTEXT = ''
    QCHOOSES = []
    QANSWER = []
    if tmp=='' :
        break
    if tmp[:5] == '[QDX]':
        QTEXT = tmp[5:]
        tmp =f.readline().decode('utf-8')
        while tmp[:3]!='[A]':
            QCHOOSES.append(tmp)
            tmp = f.readline().decode('utf-8')
        if tmp[:3]=='[A]':
            QANSWER = tmp[4:len(tmp)-2].lower().split(',')
        q = Question(qtype='dx',title_id=title_id,questiontext=QTEXT,answer=json.dumps(QANSWER),chooses=json.dumps(QCHOOSES))
        db.session.add(q)
    if tmp[:5] == '[QPD]':
        QTEXT = tmp[5:]
        print QTEXT.encode('utf-8')
        tmp =f.readline().decode('utf-8')
        if tmp[:3]=='[A]':
            QANSWER =[ int(tmp[4:len(tmp)-2]) ]
        q = Question(qtype='pd',title_id=title_id,questiontext=QTEXT,answer=json.dumps(QANSWER),chooses=json.dumps(QCHOOSES))
        db.session.add(q)

db.session.commit()