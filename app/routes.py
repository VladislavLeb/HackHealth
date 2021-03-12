from app import app, db
from flask import render_template, jsonify
from app.models import MapPoints

@app.route('/')
@app.route('/index')
def index():
    point = MapPoints.query.all()
    db.session.add(point)
    db.session.commit()
    return point.to_dict()
    # user = {'username': 'Vladislav'}
    # return render_template('index.html', title='Home', user=user)