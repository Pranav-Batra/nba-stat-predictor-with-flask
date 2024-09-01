import sqlite3 as sq
from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField
from wtforms.validators import DataRequired
import os.path

app = Flask(__name__)

my_path = "/Users/pranav/Downloads/nba stat predictor website - flask/flaskr/players.db"

pathname = "/Users/pranav/Downloads/nba stat predictor website - flask/flaskr/players.txt"

allPlayers = []
if os.path.isfile(pathname):
    file = open(pathname, 'r')
    allPlayers = file.read().splitlines()
    file.close()

@app.route('/', methods = ["GET", "POST"])
def home():
    #autocomplete_input = StringField('autocomplete_input', validators=[DataRequired()])
    if request.method == "POST":
        player_name = request.form.get('fname')
        return redirect(url_for("actual", player_name = player_name))
    return render_template("mainPage.html", allPlayers = allPlayers)

@app.route('/actual')
def actual():
    player_name = request.args.get('player_name')
    if os.path.isfile(my_path):
        conn = sq.connect(my_path)
        conn.row_factory = sq.Row
        cur = conn.cursor()
        rowsOne = cur.execute("SELECT * FROM PlayersWithFeatureCols WHERE Player = ?", (player_name,)).fetchall()
        rowsTwo = cur.execute("SELECT * FROM `2024-2025 Predicted Points Per Game` WHERE Player = ?", (player_name,)).fetchall()
        if len(rowsOne) == 0:
            return "Player Not Found"
    return render_template("players.html", player_name = player_name, rowsOne = rowsOne, rowsTwo = rowsTwo)


if __name__ == '__main__':
    app.run()