from flask import Flask, redirect, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template('submit_photo.html');

app.run(host='0.0.0.0', port=8080, debug=True)