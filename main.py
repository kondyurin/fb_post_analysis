from flask import Flask
import json
import requests
from settings import access_token

page_id = '509679185734909'
post_limit = 3 # нестабильное отображение постов

app = Flask(__name__)

@app.route("/")
def index():
    url = 'https://graph.facebook.com/v2.8/{}/feed?limit={}&access_token={}'.format(page_id, post_limit, access_token)

    r = requests.get(url)
    data = json.loads(r.text)
    result = ''
    result += "<table border=1>"
    for item in data['data']:
        result += '<tr><td>%s</td></tr>' % item['message']
    result += "</table>"

    return result

if __name__ ==  '__main__':
    app.run(port = 5020, debug = True)