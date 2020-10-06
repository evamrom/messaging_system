from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(128))
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    # def __repr__(self):
    #     return '<User %r>' % (self.username)

class Channels(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    from_user = Column(Integer, ForeignKey('users.id'))
    to_user = Column(Integer, ForeignKey('users.id'))

class Messages(Base):
    __tablename__ = 'messages'
    message = Column(Text)
    from_user = Column(Integer, ForeignKey('users.id'))
    to_user = Column(Integer, ForeignKey('users.id'))
    channel_id = Column(Integer, ForeignKey('channels.id'))