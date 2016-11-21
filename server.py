from flask import Flask, render_template, request
from db import db_session, Message, User


app = Flask(__name__)



@app.route("/")
def index():
    user_id = request.args.get('user_id')
    posts = db_session.query(Message)
    if user_id:
        posts = posts.filter(Message.user_id == user_id)
    posts = posts.order_by(Message.id)
    return render_template('index.html', posts=posts.all())

# @app.route('/filter')
# def filter():
# 	post = db_session.query(Message)
# 	if request.args.get('rgsgsse'):
# 		post = post.filter(User.first_name == request.args.get('rgsgsse'))

# 	post = post.order_by(Message.id).all()

# 	user = db_session.query(User).order_by(User.id).first()
# 	result = ''
# 	result += '<table border=1>'
# 	if post.text:
# 		result += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(post.fb_id, post.updated_time, post.created_time, post.text)
# 	result += '</table>'
# 	return result

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)
