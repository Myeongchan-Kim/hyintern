#-*- coding: utf-8 -*-
# encoding=utf8
#flaskr.py

from __future__ import with_statement
from contextlib import closing

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3
from flask import Flask, request, session, g, redirect, url_for , \
	abort, render_template, flash, make_response
from flask import json


#configuartion
DATABASE = '/tmp/hyintern.db'
DEBUG = True
SECRET_KEY = 'hanyang'
USERNAME = 'admin'
PASSWORD = 'default'
LOCATION = {'seoul':'서울', 'guri':'구리', 'chang':'창원', 'jeju':'제주'}

# create our little app.
app = Flask(__name__)
app.config.from_object(__name__)

# set location by cookie
if(hasattr(request ,'cookie')):
    location_cookie = request.cookie.get('location')
else :
    location_cookie = 'guri'

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()


@app.route('/')
def index_page():
    return redirect(url_for('show_phone_num_list', location=location_cookie))


@app.route('/show/<location>', methods=['GET'])
def show_phone_num_list(location = location_cookie):
    query = "select title, phone_num from phone_num_list where location='%s' order by id desc" % location
    cur = g.db.execute(query)
    
    phone_num_list = [dict(title=row[0], phone_num=row[1]) for row in cur.fetchall()]
    resp = make_response(render_template('show_phone_num_list.html', list=phone_num_list, location_str=location))
    resp.set_cookie('location', location)
    print(location)
    return resp



@app.route('/edit', methods=['GET'])
def edit_mode():
    if not session.get('logged_in'):
        abort(401)
    cur = g.db.execute('select id, title, phone_num, location from phone_num_list order by id desc')
    phone_num_list = [dict(id=row[0], title=row[1], phone_num=row[2], location=row[3]) for row in cur.fetchall()]
    return render_template('edit_mode.html', list=phone_num_list )


@app.route('/add', methods=['POST'])
def add_phone_num():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into phone_num_list (title, phone_num, location) values (?, ?, ?)',
                 [request.form['title'], request.form['phone_num'] , request.form['location']])
    g.db.commit()
    flash('New phone number was successfully posted')
    return redirect(url_for('index_page'))

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id=None):
    if not session.get('logged_in'):
        abort(401)
    query = "delete from phone_num_list where id= '%s'" % request.form['id'] 
    #print("query : ",query)
    g.db.execute(query)
    g.db.commit()
    flash(id+'has deleted')
    return redirect(url_for('edit_mode'), code='303')



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_phone_num_list', location=location_cookie))
    if(('logged_in' in session) and (session['logged_in'] == True)) :
        return redirect(url_for('show_phone_num_list'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_phone_num_list', location=location_cookie))
    
if __name__ == '__main__':
	#app.DEBUG = True;
	app.run(host='0.0.0.0', port=80)
