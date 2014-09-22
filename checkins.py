import os
import flask
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config.update(DEBUG = True,)


@app.route('/', methods=['GET','POST'])
def index(name=None):
	return " Hello index"
	#return render_template('checkins.html')

@app.route('/checkins', methods=['GET','POST'])
def checkins(name=None):
	return "hello "
	#return render_template('inside.html')

if __name__ == '__main__':
	port = int(os.environ.get("DEV_PORT", 5003))
	app.run(debug=True,host='0.0.0.0',port=port)