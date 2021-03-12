from app import db

class MapPoints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pointX = db.Column(db.Float, index=True, unique=True)
    pointY = db.Column(db.Float, index=True, unique=True)
    name = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.name) 