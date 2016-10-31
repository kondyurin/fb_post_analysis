import json
import requests
import datetime 
from settings import access_token
from db import db_session, Message, User

page_id = '509679185734909'
post_limit = 10 
messages_list = []

def add_post_to_db():
    url = "https://graph.facebook.com/v2.8/{}/feed?fields=updated_time,message,from,attachments,likes&limit={}&access_token={}".format(page_id, post_limit, access_token)
    r = requests.get(url)
    data = r.json()

    for item in data['data']:
        messages_list.append(item)

    for message_data in messages_list:
        print(message_data)

        user = User(fb_id = message_data['from']['id'], name = message_data['from']['name'])
        message_data['updated_time'] = datetime.datetime.strptime(message_data['updated_time'], '%Y-%m-%dT%H:%M:%S+%f')
        message_result = Message(author = user, fb_id = message_data['id'], updated_time = message_data.get('updated_time', ''), text = message_data.get('message', ''))

        db_session.add(message_result)
    db_session.commit()

    return 'OK'

if __name__ ==  '__main__':
    add_post_to_db()



#1. Добавить проверку перед добавлением на наличие записи в БД