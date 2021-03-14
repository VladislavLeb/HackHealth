from app import db

class MapPoints(db.Model):
    serialize_only = ('id', 'name', 'city', 'pointX', 'pointY')

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), index=True, unique=False)
    name = db.Column(db.String(120), index=True, unique=False)
    description = db.Column(db.String(1000), index=True, unique=False)
    pointX = db.Column(db.Float, index=True, unique=False)
    pointY = db.Column(db.Float, index=True, unique=False)

    def __repr__(self):
        return '<Sightseen name {}, city {}, desc {}, pointX {}, pointY {}>'.format(self.name, self.city, self.description, self.pointX, self.pointY) 

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'city'       : self.city,
           'name'       : self.name,
           'pointX'     : self.pointX,
           'pointY'     : self.pointY
       }

class MapRoutes(db.Model):
    serialize_only = ('id', 'city', 'routeName', 'mapPointNames')

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), index=True, unique=False)
    routeName = db.Column(db.String(120), index=True, unique=False)
    mapPointNames = db.Column(db.String(400), index=True, unique=False)

    def __repr__(self):
        return '<Sightseen city {}, routeName {}, mapPointNames {}>'.format(self.city, self.routeName, self.mapPointNames) 

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'             : self.id,
           'city'           : self.city,
           'routeName'      : self.routeName,
           'mapPointNames'  : self.mapPointNames
       }