import json
import requests
import datetime 
from settings import access_token
from db import db_session, Message, User

page_id = '509679185734909' #id группы FB
post_limit = 5 #кол-во загружаемых постов

def add_post_to_db():
    url = "https://graph.facebook.com/v2.8/{}/feed?fields=updated_time,message,from,attachments,likes&limit={}&access_token={}".format(page_id, post_limit, access_token)

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        print('not 200 OK')

    for message_data in data['data']:
        # создаем экземпляр класса User с именованными аргументами, которые необходимо заполнять в БД
        user = User(fb_id = message_data['from']['id'], name = message_data['from']['name'])
        # конвертируем дату в python data
        message_data['updated_time'] = datetime.datetime.strptime(message_data['updated_time'], '%Y-%m-%dT%H:%M:%S+%f')
        # создаем экземпляр класса Message с именованными аргументами, которые необходимо заполнить в БД
        message_result = Message(author = user, fb_id = message_data['id'], updated_time = message_data.get('updated_time', ''), text = message_data.get('message', ''))

        fb_id_check = message_data['id']
        # получаем список id постов уже имеющихся в базе
        test = db_session.query(Message).filter(Message.fb_id == fb_id_check).all()
        
        print(fb_id_check)
        print(len(test))

        # проверяем наличие поста в БД и в случае отсутствия добавляем в базу
        if len(test) == 0:
            db_session.add(message_result)
    db_session.commit()

    return 'OK'

if __name__ ==  '__main__':
    add_post_to_db()



#1. Добавить проверку перед добавлением на наличие записи в БД +
#2. Добавить проверку на коррекность ответа сервара для json +
#3. Реализовать запуск скрипта по крону
#4. Реализовать автонаполнение базы
#5. Расширить БД новыми таблицами
#6. Проверять значения текст на пустые 
#7. Сделать обработку постов
