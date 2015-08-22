#-*- coding: utf-8 -*-
#flaskr.py

from __future__ import with_statement
from contextlib import closing

import sqlite3
from flask import Flask, request, session, g, redirect, url_for , \
	abort, render_template, flash
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
def show_phone_num_list():
	cur = g.db.execute('select title, phone from phone_num_list order by id desc')
	phone_num_list = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('show_phone_num_list.html', list=phone_num_list)

'''
@app.route('/input_page', methods= ['GET'])
def input_page():
	if not session.get('logged_in'):
        abort(401)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into phone_num_list (title, phone) values (?, ?)',
                 [request.form['title'], request.form['phone']])
    g.db.commit()
    flash('New phone number was successfully posted')
    return redirect(url_for('phone_num_list'))

'''
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
            return redirect(url_for('show_phone_num_list'))
    if(('logged_in' in session) and (session['logged_in'] == True)) :
        return redirect(url_for('show_phone_num_list'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_phone_num_list'))

if __name__ == '__main__':
	app.DEBUG = True;
	app.run()
