#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from bottle import Bottle, route, run, template, get, post, debug, static_file, request, redirect, response
import time
import random
import string
import logging
from users import users
import logging.handlers
import sqlite3

log = logging.getLogger('bottle')
log.setLevel('INFO')
h = logging.handlers.TimedRotatingFileHandler(
    'logs/nlog', when='midnight', backupCount=9999)
f = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
h.setFormatter(f)
log.addHandler(h)

secretKey = "SDMDSIUDSFYODS&TTFS987f9ds7f8sd6DFOUFYWE&FY"

app = Bottle()


@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='./static')


def checkAuth():
    loginName = request.get_cookie("user", secret=secretKey)
    randStr = request.get_cookie("randStr", secret=secretKey)
    log.info(str(loginName) + ' ' + request.method + ' ' +
             request.url + ' ' + request.environ.get('REMOTE_ADDR'))
    if (loginName in users) and (users[loginName].get("randStr", "") == randStr) and (
            users[loginName]["loggedIn"]) and (time.time() - users[loginName]["lastSeen"] < 3600):
        users[loginName]["lastSeen"] = time.time()
        return loginName
    return redirect('/login')


@app.route('/register')
@app.route('/register')
@app.route('/register', method='POST')
def register():
    # Tutaj ściągnij z formularza wszystkie informacje, które chcesz zapisać
    country = request.forms.get('country', default=False)
    city = request.forms.get('city', default=False)

    with sqlite3.connect('webapp.db') as connection:
        cursor = connection.cursor()
        address_id = cursor.execute(
            f"SELECT id_address FROM Address_Entities WHERE city='{city}' AND country='{country}'"
        ).fetchone()  # odpowiedź postaci: (ID,)
        if address_id is None:
            cursor.execute(f"INSERT INTO Address_Entities (city, country) VALUES('{city}','{country}')", )
            address_id = cursor.execute(f"SELECT MAX(id_address) FROM Address_Entities").fetchone()[0]
        else:
            address_id = address_id[0]

        print(address_id)
        # w tym miejscu masz pod address_id
        # bądź istniejącego wcześniej rekordu address, bądź właśnie stworzonego

    return template('login')


@app.route('/login')
@app.route('/login/')
@app.route('/login', method='POST')
def login():
    loginName = request.forms.get('login_name', default=False)
    password = request.forms.get('password', default=False)
    randStr = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(18))
    log.info(str(loginName) + ' ' + request.method + ' ' +
             request.url + ' ' + request.environ.get('REMOTE_ADDR'))
    if (loginName in users) and users[loginName]["password"] == password:
        response.set_cookie("user", loginName, secret=secretKey)
        response.set_cookie("randStr", randStr, secret=secretKey)
        users[loginName]["loggedIn"] = True
        users[loginName]["randStr"] = randStr
        users[loginName]["lastSeen"] = time.time()

        redirect('/index')
        return True
    else:
        return template('login')


@app.route('/')
@app.route('/index')
@app.route('/index/')
@app.route('/index/<message>')
def index(message=''):
    loginName = checkAuth()
    messDict = {'error': "Something went wrong",
                'ok': "Everything is ok."}

    name = request.forms.get('name', default=False)
    yearFrom = request.forms.get('yearFrom', default=False)
    yearTo = request.forms.get('yearTo', default=False)

    query = f"""
        SELECT S.Date, S.AltmanScore, S.AltmanRating 
        FROM Score_Rating S 
            JOIN Reference_Data_Entities R 
                ON S.ID_Entities = R.ID_Entities
        WHERE R.Name = '{name}'
            AND S.Date BETWEEN {yearFrom} AND {yearTo}"""

    with sqlite3.connect('webapp.db') as connection:
        cursor = connection.cursor()
        scores = cursor.execute(query).fetchall()  # [(Date, AltmanScore, AltmanRating),(...),(...)]

    return template('index', message=messDict.get(message, ""), loginName=loginName, scores=scores)


@app.route('/logout', method='GET')
def logout():
    username = request.get_cookie("user", secret=secretKey)
    users[username]["loggedIn"] = False
    response.set_cookie("user", None, secret=secretKey)
    response.set_cookie("randStr", None, secret=secretKey)
    return template('login')


@app.route('/action1')
def action1():
    loginName = request.get_cookie("user", secret=secretKey)
    if loginName is None:
        return template('action1')
    else:
        return template('index', loginName=loginName)


app.run(host='localhost', port=65518, reloader=False, debug=False)
