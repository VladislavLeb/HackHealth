from app import db
from sqlalchemy_serializer import SerializerMixin

class MapPoints(db.Model, SerializerMixin):
    serialize_only = ('id', 'name', 'pointX', 'pointY')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    pointX = db.Column(db.Float, index=True, unique=False)
    pointY = db.Column(db.Float, index=True, unique=False)

    def __repr__(self):
        return '<Sightseen name {}, pointX {}, pointY {}>'.format(self.name, self.pointX, self.pointY) 