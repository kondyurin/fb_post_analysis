import pymorphy2
import re
from collections import defaultdict, Counter
from db import db_session, Message
from metro_stations import metro_stations

def exlude_stop_words():
    pass

def dict_freq():
    pass

def get_message_text(): #корректная функция
    text_list = []
    text = db_session.query(Message)
    for item in text.all():
        text_list.append(item.text)
    return text_list

def split_message_text(): #корректная функция
    messages = []
    for item in get_message_text():
        result = re.sub('[^\w\d\s\n]', '', item).replace('\n', '').lower()
        fb_words = result.split(" ")
        messages.append(fb_words)
    return messages

def first_word_dict_freq(): #Сделать частотный словарь!
    i = 0
    while split_message_text():
        result = dict(Counter(split_message_text())) #использовать list.pop()
    # for item in split_message_text():
    #     print(item)
    # d = defaultdict(int)
    # for k in split_message_text():
    #     d[k] += 1
    # print(d.items())
    print(result)

def get_word_lexeme(input_word):
    m = pymorphy2.MorphAnalyzer()
    lexeme_list = m.parse(input_word)[0].lexeme
    result = [item.word for item in lexeme_list]
    return result

def find_metro_intersection(): #корректная функция
    i = 0
    message_metro = []
    for item in split_message_text():
        metro_in_message = list(set(item).intersection(metro_stations)) #ищем пересечение станций метро и текта сообщений
        if metro_in_message:
            message_metro.append(metro_in_message[0])
            message_metro = list(set(message_metro)) #оставляем уникальные названия станции метро в итоговом списке
            i += 1
    return sorted(message_metro)
    # print(message_metro)
    # print(i)

def find_type_of_message(): #корректная функция
    i = 0
    words_list = ['сдавать', 'сдать', 'искать']
    for word in words_list:
        search_phrase = get_word_lexeme(word)
        for item in split_message_text():
            first_word = item[0]
            if first_word in search_phrase:
                i += 1
                print('{}'.format(first_word))
    print(i)

def find_metro_regex():
    pass

# split_message_text()
# get_word_from_db()
# get_word_lexeme('сдать')
# find_metro_intersection()
# find_type_of_message()
# first_word_dict_freq()
# get_message_text()

#TODO:
#составить список станций метро DONE
#проверять вхождение станции метро в пост DONE 
#реализовать проверку вхождений во всех постах: 2091 пост с точным совпадением станции метро DONE
#реализовать определение типа сообщения: сдам сниму и т.п. Для начала сделать для одной фразы DONE
#очистить от стоп-слов; привести к начальной форме; сделать частотный словарь для первых слов и для всех слов; сравнить;
#реализовать определение типа сообщения: сдам сниму и т.п. Сделать для списка фраз, которые будут наиболее частыми по частотному словарю
#класть значение станции метро в базу к соответствующей записи

def find_metro_intersection_old():
    pass
#     i = 0
#     #взять из базы одну запись из которой вытащить message
#     text = db_session.query(Message)#.filter(Message.user_id == '7368')
#     for message in text.all():
#         result = re.sub('[^\w\d\s\n]', '', message.text).replace('\n', '').lower()
#         fb_words = result.split(' ')
#         #ищем тупым пересечением множеств
#         result = list(set(fb_words).intersection(metro_stations))
#         if result:
#             print('{} - id: {}'.format(result, message.id))
#             i += 1
#     print(i)
#     return result

def find_type_of_message_old():
    pass
#     i = 0
#     #взять из базы одну запись из которой вытащить message
#     text = db_session.query(Message)#.filter(Message.user_id == '7368')
#     search_phrase = get_word_lexeme('сдать')
#     for message in text.all():
#         result = re.sub('[^\w\d\s\n]', '', message.text).replace('\n', '').lower()
#         fb_words = result.split(' ')
#         first_word_in_message = fb_words[0]
#         if first_word_in_message in search_phrase:
#             i += 1
#             print('{} - {}'.format(first_word_in_message, message.id))
#     print(i)
#         # result = list(set(first_word_in_message).intersection(search_phrase))
#         # print(result)
#         # if message.text:
#         #     try:
#         #         # print('{} - {}'.format(fb_words[0], i))
#         #         result = list(set(fb_words).intersection(get_word_lexeme()))
#         #         print('{} - {}'.format(result, i))
#         #     except IndexError:
#         #         pass 
#     # return '1'