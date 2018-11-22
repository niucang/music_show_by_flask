from flask import Flask
from flask import render_template
import os
import re

app = Flask(__name__)
@app.route("/")
def hello():
    music_list = os.listdir(os.getcwd() + '/static/musics')
    return render_template('player.html', music_list = music_list, re = re)

if __name__ == "__main__":
    app.run(debug = True)
