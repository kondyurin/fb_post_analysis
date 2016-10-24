from flask import Flask
from db import db_session, Messages

app = Flask(__name__)

@app.route("/")
def index():
    posts = db_session.query(Messages).all()
    result = ''

    result += "<table border=1>"
    for item in posts:
        if item.message:
            result += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(item.id, item.updated_time, item.message)
            
    result += "</table>"
    return result

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)