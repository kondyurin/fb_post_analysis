from flask import Flask, render_template, request
from db import db_session, Message

app = Flask(__name__)

@app.route("/")
def index():
    user_id = request.args.get("user_id")
    posts = db_session.query(Message)
    if user_id:
        posts = posts.filter(Message.user_id.like("%{}%".format(user_id)))

    return render_template('index.html', posts=posts.all())

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)
