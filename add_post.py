import json
import requests
from settings import access_token
from db import db_session, Messages

page_id = '509679185734909'
post_limit = 5 # нестабильное отображение постов
messages_list = []

def add_post_to_db():
    url = 'https://graph.facebook.com/v2.8/{}/feed?limit={}&access_token={}'.format(page_id, post_limit, access_token)

    r = requests.get(url)
    data = r.json()
    for item in data['data']:
        messages_list.append(item)

    for message_data in messages_list:
        message_result = Messages(message_data['updated_time'], message_data.get('message', ''))
        
        db_session.add(message_result)

    db_session.commit()

    return 'OK'

if __name__ ==  '__main__':
    get_post_from_db()