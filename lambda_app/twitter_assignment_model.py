from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String,nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)

class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    body = DB.Column(DB.Unicode(260))
    username_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)
    username = DB.relationship('User', backref=DB.backref("tweet", lazy=True))

    def __repr__(self):
        return "<Tweet: {}".format(self,name)