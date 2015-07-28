#routingTest.py

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'hello_route!'

@app.route('/student/<username>')
def student(username):
	return 'Hello %s' % username

@app.route('/student/<username>/<int:user_id>')
def student_with_id(username, user_id):
	return 'Hello %s , %d' %(username, user_id)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')

