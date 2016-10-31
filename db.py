from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    fb_id = Column(Integer)
    name = Column(String(50))
    message = relationship('Message', backref = 'author')

    # def __init__(self, fb_id = None, name = None):
    #     self.fb_id = fb_id
    #     self.name = name

    def __repr__(self):
        return '<User {} {}>'.format(self.fb_id, self.name)

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    fb_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    updated_time = Column(DateTime)
    text = Column(Text)

    # def __init__(self, fb_id=None, updated_time=None, text=None):
    #     self.fb_id = fb_id
    #     self.updated_time = updated_time
    #     self.text = text
    #     self.user_id = user_id

    def __repr__(self):
        return '<Message {} {}>'.format(self.fb_id, self.updated_time, self.text)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)