from flask import Flask, render_template
from db import db_session, Message

app = Flask(__name__)

@app.route("/")
def index():
    posts = db_session.query(Message).all()
    print(posts)

    return render_template('index.html', posts=posts)

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)
