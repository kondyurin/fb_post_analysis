from flask import Flask, render_template, request
from db import db_session, Message
from morph import find_metro_intersection

app = Flask(__name__)

@app.route("/")
def index():
    text = request.args.get("text")
    posts = db_session.query(Message)

    if text:
        posts = posts.filter(Message.text.like("%{}%".format(text)))

    return render_template('index.html', posts=posts.all(), metro_station=find_metro_intersection())

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)
