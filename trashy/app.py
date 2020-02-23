from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from flask_bootstrap import bootstrap
import requests

app = Flask(name)


@app.route('/')
def index():
    return render_template("home.html")

def printing(str):
    str = str+"sheep"
    print(str)

@app.route("/info", methods=['POST'])
def echo():
    return render_template('home.html', text=printing(request.form['text']))




if name == 'main':
    app.secret_key= 'secret123'
    app.run(debug=True)