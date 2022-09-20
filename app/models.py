from app.database import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
