#getTest.py

from flask import Flask
from flask import request, url_for

app = Flask(__name__)

@app.route('/method', methods=['GET', 'POST'])
def test_HTTP_method():
	if request.method == 'POST':
		return request.method
	else :
		return request.method + '<p>' + request.args.get('name') + '<p>' + request.args.get('password')

if __name__ == '__main__' :
	app.debug = True
	app.run()