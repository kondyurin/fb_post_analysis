from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    updated_time = Column(String(50))
    message = Column(Text(2000))
    # posts = relationship('Post', backref='author')

    def __init__(self, updated_time=None, message=None):
        self.updated_time = updated_time
        self.message = message

    def __repr__(self):
        return '<Message {} {}>'.format(self.updated_time, self.message)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)