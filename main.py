from flask import Flask
import json
import requests
from settings import access_token
from db import db_session, Messages

page_id = '509679185734909'
post_limit = 10 # нестабильное отображение постов
messages_list = []

app = Flask(__name__)

@app.route("/")
def index():
    url = 'https://graph.facebook.com/v2.8/{}/feed?limit={}&access_token={}'.format(page_id, post_limit, access_token)

    r = requests.get(url)
    data = r.json()
    for item in data['data']:
        messages_list.append(item)

    for message_data in messages_list:
        print(message_data)
        message_result = Messages(message_data['updated_time'], message_data.get('message', ''))
        db_session.add(message_result)

    db_session.commit()

    # result = ''
    # result += "<table border=1>"
    # for item in data['data']:
    #     print(item.get('message', 'No message in item'))
    #     result += '<tr><td>%s</td></tr>' % item.get('message', 'no message')
    # result += "</table>"

    return 'OK'

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)