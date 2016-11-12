import pymorphy2
import re
from db import db_session, Message

m = pymorphy2.MorphAnalyzer()

def split_message():
    #взять из базы одну запись из которой вытащить message
    text = db_session.query(Message).filter(Message.user_id == '1')
    regex = re.compile('[^\w\d\s\-\n\.\(\)\{\}\[\]\"\'«»`%,:_]')
    for message in text.all():
        result = regex.findall(string, pos=None, endpos=None)
    return print(result)

split_message()