from lambda_app.twitter_assignment_model import User, Tweet, DB
from flask import Flask, request
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB.init_app(app)

@app.route('/')
def landing():
    gp = User(id=1, name="gp")
    jpo = User(id=3, name='jpo')
    jp = User(id=2, name='jp')
    tweet = Tweet(id=1, body='NOcoy', username=gp)
    tweet2 = Tweet(id=2, body='sitcoy', username=jp)
    tweet3 = Tweet(id=3, body='yaaa', username=jpo)
    DB.session.add(jpo)
    DB.session.add(tweet3)
    DB.session.commit()
    users = User.query.all()
    return 'hello world, my name is GP' + ', '.join([u.name for u in users])

if __name__ == '__main__':
    app.run()
