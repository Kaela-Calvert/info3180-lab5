from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy

class Movie(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    poster = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, id, title, description, poster, created_at):
        self.id=id
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at
          
    def __repr__(self):
        return '<Movie %f>' % (self.title)