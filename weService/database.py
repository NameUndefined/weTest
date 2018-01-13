import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= \
    'sqlite:///'+os.path.join(basedir,'database.sqlite')

db = SQLAlchemy(app)
db.init_app(app)
class Question(db.Model):
    __tablename__='questions'
    id = db.Column(db.Integer,primary_key=True)
    qtype = db.Column(db.Integer)
    title_id=db.Column(db.Integer,db.ForeignKey('titles.id'))
    questiontext=db.Column(db.Text)
    answer = db.Column(db.Text)
    chooses = db.Column(db.Text)
    def to_json(self):
        json_question={
                'id':self.id,
                'qtype':self.qtype,
                'title_id':self.title_id,
                'questiontext':self.questiontext,
                'answer':self.answer,
                'chooses':self.chooses
                }
        return json_question
    def __repr__(self):
        return '<Question %r>' % self.questiontext

class Title(db.Model):
    __tablename__='titles'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text,unique=True)
    questions = db.relationship('Question',backref='title')
    def to_json(self):
        json_title={
                'id':self.id,
                'title':self.title
                }
        return json_title
    def __repr__(self):
        return '<Title %r>' % self.title
class Article(db.Model):
    __tablename__='articles'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.Text,unique=True)
    url=db.Column(db.Text)
    intro =db.Column(db.Text)
    def to_json(self):
        json_title={
                'id':self.id,
                'title':self.title,
                'url':self.url,
                'intro':self.intro
                }
        return json_title
    def __repr__(self):
        return '<Article %r>' % self.title
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    userNick = db.Column(db.Text,unique=True)
    userIMEI = db.Column(db.Text,unique=True)
    userPw = db.Column(db.Text)
    def to_json(self):
        json_user={
                'id':self.id,
                'nick':self.userNick,
                'imei':self.userIMEI
                }
        return json_user
    def __repr__(self):
        return '<User %r>' % self.userIMEI

class Record(db.Model):
    __tablename__='records'
    id=db.Column(db.Integer,primary_key=True)
    userScore = db.Column(db.Integer)
    userIMEI = db.Column(db.Text) #unique
    titleID = db.Column(db.Integer)
    wrongQuestions = db.Column(db.Text)
    def to_json(self):
        json_user={
                'id':self.id,
                'score':self.userScore,
                'imei':self.userIMEI,
                'titleID':self.titleID,
                'wrong':self.wrongQuestions
                }
        return json_user
    def __repr__(self):
        return '<Record score %r>' % self.userScore


