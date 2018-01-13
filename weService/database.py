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

    

