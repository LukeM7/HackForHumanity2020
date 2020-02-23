from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from PIL import Image
import os
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/processImage', methods=['POST'])
def processImage():
    if request.method == 'POST':
        image = request.files.get("myFile")
        print(image)
        im = Image.open(image, mode='r')#im is a pillow object

        im.save('userImages/userim.png')

    return render_template("home.html")

@app.route("/info", methods=['POST'])
def echo():
    return render_template('home.html', text=printing(request.form['text']))


if __name__ == '__main__':
    app.secret_key= 'secret123'
    app.run(debug=True)
