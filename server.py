from flask import Flask, render_template, request
from db import db_session, Message
from morph import find_metro_intersection
from add_post import add_post_to_db

app = Flask(__name__)

@app.route("/")
def index():
    text = request.args.get("text")
    posts = db_session.query(Message)
    posts_count = db_session.query(Message).count()

    if text:
        posts = posts.filter(Message.text.like("%{}%".format(text)))

    return render_template('index.html', posts=posts.all(), metro_station=find_metro_intersection(), db_time_update=add_post_to_db(), posts_count=posts_count)

@app.route("/objects")
def objects():
    return render_template('objects.html')

@app.route("/stat")
def stat():
    return render_template('stat.html')

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)
