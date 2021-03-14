# -*- coding: utf-8 -*-
from app import app, db
from flask import render_template, jsonify, request
import json
from app.models import MapPoints, MapRoutes

@app.route('/')
@app.route('/index')
def index():
    # point = MapPoints.query.filter_by(id=8).first()
    # point.description = 'Арт-объект “Прыпынак Адамовича”, является первым проектом в рамках компании по увековечиванию памяти Алеся Адамовича, инициативной группой “Прыпынак Адамовича”. Идея создания арт-объекта заключалось в том чтобы привлечь внимание к творчеству и личности Алеся Адамовича и к проблеме что он не был увековечен. Данная остановка инициативой была не случайно, центральную улицу Октябрьскую хотели переименовать в 90-х, но власть решила назвать пересекающую тут рядом улицу в честь него. Здесь рядом находится дом Алеся Адамовича в котором он жил после войны. Возле дома можете увидеть три березы, которые вы встретите в строках на остановке. Он считал его своей малой родиной, хоть он и родился в другом месте. Здесь снимался один из первых фильмов по его книге Туровым. Он был реализован в сентябре 2018 году и презентован в рамках фестиваля “Глушанский хуторок”. Автор Алесь Благий'
    # db.session.commit()
    #  db.session.add(point)
    # point = MapPoints(name = "Памятник Алесю Адамовичу", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.087486, pointY = 28.854656)
    # db.session.add(point)
    # point = MapPoints(name = "Могила Алеся Адамовича", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.087486, pointY = 28.854656)
    # db.session.add(point)
    # point = MapPoints(name = "Могила матери Алеся Адамовича", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.087486, pointY = 28.854656)
    # db.session.add(point)
    # point = MapPoints(name = "Мельница", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.091687, pointY = 28.865772)
    # db.session.add(point)
    # point = MapPoints(name = "Старообрядческая церковь", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.091200, pointY = 28.866491)
    # db.session.add(point)
    # point = MapPoints(name = "Гончарная", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.091365, pointY = 28.865078)
    # db.session.add(point)
    # point = MapPoints(name = "арт-объект Прыпынак Адамовича", city = 'п. Глуша (Бобруйский р-н)', pointX = 53.087824, pointY = 28.865188)
    # db.session.add(point)

    # newRoute = MapRoutes(city = 'п. Глуша (Бобруйский р-н)', routeName = 'Жизнь Алеся Адамовича', mapPointNames = 'арт-объект Прыпынак Адамовича, Могила матери Алеся Адамовича, Могила Алеся Адамовича, Памятник Алесю Адамовичу, Аптека')
    # db.session.add(newRoute)
    # newRoute = MapRoutes(city = 'п. Глуша (Бобруйский р-н)', routeName = 'Музей ремесел', mapPointNames = 'Гончарная, Старообрядческая церковь, Мельница')
    # db.session.add(newRoute)
    # db.session.commit()
    # return jsonify(json_list=[i.serialize for i in MapRoutes.query.all()])
    # return jsonify(json_list = MapPoints.query.all())
    user = {'username': 'Vladislav'}
    return render_template('index.html', title='Home', user=user)

@app.route('/select-route')
def selectRoute():
    # routesJson = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }, 
    #     {
    #         'author': {'username': 'Ипполит'},
    #         'body': 'Какая гадость эта ваша заливная рыба!!'
    #     }
    # ]
    routes = [i.serialize for i in MapRoutes.query.all()]
    title = 'Выбор маршрута'
    title = title.decode('utf-8')
    return render_template('selectRoute.html', title=title, routes=routes)
    # return jsonify(json_list=[i.serialize for i in MapRoutes.query.all()])

@app.route('/select-point')
def selectPoint():
    points = [i.serialize for i in MapPoints.query.all()]
    title = 'Выбор точки'
    title = title.decode('utf-8')
    return render_template('selectPoint.html', title=title, points = points)

@app.route('/build-route', methods=['GET'])
def buildRoute():
    pointDesc = []
    routeId = request.args.get('routeId')
    route = MapRoutes.query.get(routeId)
    pointNamesList = route.mapPointNames.split(",")
    rtt = 'pedestrian'
    url = 'https://yandex.ru/map-widget/v1/?rtext='
    for pointName in pointNamesList:
        point = MapPoints.query.filter_by(name=pointName.strip()).first()
        pointDesc.append([point.name, point.description])
        url = url + str(point.pointX) + "%2C" + str(point.pointY) + "~"
    url = url[:len(url) - 1]
    url = url + "&rtt=" + rtt
    return render_template('map.html', routeName = route.routeName, url = url, pointDesc = pointDesc)

@app.route('/goto-point', methods=['GET'])
def gotoPoint():
    zoom = '14'
    pointId = request.args.get('pointId')
    point = MapPoints.query.get(pointId)
    url = 'https://yandex.ru/map-widget/v1/?rtext='
    url = url + str(point.pointX) + "%2C" + str(point.pointY) + "~"
    url = url[:len(url) - 1]
    url = url + "&z=" + zoom
    return render_template('map.html', url = url, desc = point.description)

@app.route('/map', methods=['GET'])
def openMap():
    return render_template('map.html')