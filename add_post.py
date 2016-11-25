import json
import requests
import datetime 
from settings import access_token
from db import db_session, Message, User, Image

page_id = '509679185734909' #id группы FB
post_limit = 100 #кол-во загружаемых постов

def add_post_to_db():

    """ Заполнение таблиц БД. """

    url = "https://graph.facebook.com/v2.8/{}/feed?fields=updated_time,created_time,message,from,attachments,likes&limit={}&access_token={}".format(page_id, post_limit, access_token)

    next_group_page = True
    num_posts = 0
    start_time = datetime.datetime.now()

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        print('not 200 OK')

    while next_group_page:
        for message_data in data['data']:
            # создаем экземпляр класса User с именованными аргументами, которые необходимо заполнять в БД
            user = User(fb_id = message_data['from']['id'], name = message_data['from']['name'])
            # конвертируем дату в python data
            message_data['updated_time'] = datetime.datetime.strptime(message_data['updated_time'], '%Y-%m-%dT%H:%M:%S+%f')
            message_data['created_time'] = datetime.datetime.strptime(message_data['created_time'], '%Y-%m-%dT%H:%M:%S+%f')
            # создаем экземпляр класса Message с именованными аргументами, которые необходимо заполнить в БД
            message_result = Message(author = user, fb_id = message_data['id'], updated_time = message_data.get('updated_time', ''), created_time = message_data.get('created_time', ''), text = message_data.get('message', ''))

            fb_id_arg = message_data['id']
            text_arg = message_data.get('text')
            # получаем список id постов уже имеющихся в базе
            id_in_db = db_session.query(Message).filter(Message.fb_id == fb_id_arg).all()
            # делаем проверку на пустые строки в поле text
            empty_text = db_session.query(Message).filter(Message.text == text_arg).all()
            # проверяем наличие поста в БД и в случае отсутствия добавляем в базу

            if not id_in_db or empty_text:
                db_session.add(message_result)
            else:
                next_group_page = False
            num_posts += 1
            if num_posts % 100 == 0:
                print('{} done at {}, created time: {}'.format(num_posts, datetime.datetime.now(), message_data['created_time']))
        if 'paging' in data:
            r = requests.get(data['paging']['next'])
            data = r.json()
            db_session.commit()
        else:
            next_group_page = False

    return 'OK'

if __name__ ==  '__main__':
    add_post_to_db()



#1. Добавить проверку перед добавлением на наличие записи в БД +
#2. Добавить проверку на коррекность ответа сервара для json +
#6. Проверять значения текст на пустые +
#1. Добавить время создания поста "created_time" в таблицу Message +
#8. Заполнить базу постами за 2016 год +

#7. Сделать обработку постов (очистить от знаков; стоп-слов; токенизировать; привести к номальной форме)
#9. Реализовать добавление станции метро и стоимости в базу а также признака сдам/сниму
#3. Реализовать запуск скрипта по крону
#4. Реализовать автонаполнение базы
#5. Расширить БД новыми таблицами
#10. Развернуть Flask

