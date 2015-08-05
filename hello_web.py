# hello_web.py
from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello_world!'

@app.route('/login', methods= ['POST', 'GET'])
def login():
	try:
		if request.method == "POST":
			name 	= request.form['name']
			passwd 	= request.form['password']
			return "%s logged-in " % name

		else :
			return render_template('login.html')
	except KeyError, err :
		print 'err -> : ' , err
		return 'wrong request'

if __name__ == "__main__" :
	app.debug = True;
	app.run()