from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    list = {4,3,2,1,5}
    return render_template("about.html", list = list)

#example function
# class CardForm(Form):
#     title = StringField('Title', [validators.Length(min =1, max = 100)])
#     body = TextAreaField('Body', [validators.Length(min =30)])
#     restName = MultiCheckboxField('Restaurants', choices=[])


#example using python to html
# @app.route("/cards")
# def cards():
#     #create cursor, execute, commit, close
#     cur = mysql.get_db().cursor()
#     result = cur.execute("SELECT * FROM cards")#view cards?
#     cards = cur.fetchall()
#
#     if bool(result) == True:
#         return render_template('cards.html', cardZ = cards)
#     else:
#         msg = "No Cards Found"
#         return render_template('cards.html', msg = msg)
#     cur.close()


if __name__ == '__main__':
    app.secret_key= 'secret123'
    app.run(debug=True)
