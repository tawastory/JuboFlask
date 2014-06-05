from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

db_engine = create_engine('mysql://root:autoset@127.0.0.1/jubo?charset=utf8&use_unicode=1', echo=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))
metadata = MetaData()
Base = declarative_base()

class Jubo(Base):
    __tablename__ = 'jubo_am'

    id = Column(Integer, primary_key=True)
    firsthymn = Column(String(45), unique=False)
    psalm = Column(String(45), unique=False)
    secondhymn = Column(String(45), unique=False)
    scripture = Column(String(45), unique=False)
    sermon = Column(String(45), unique=False)
    offertory = Column(String(45), unique=False)
    
    def __init__(self, firsthymn, psalm, secondhymn, scripture, sermon, offertory):
        self.id = id
        self.firsthymn = firsthymn
        self.psalm = psalm
        self.secondhymn = secondhymn
        self.scripture = scripture
        self.sermon = sermon
        self.offertory = offertory

    def __repr__(self):
        return '<Jubo %r>' % (self.id)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    password = Column(String(45), unique=False)
    
    def __init__(self, id, password):
        self.id = id
        self.password = password
        
    def __repr__(self):
        return '<User %r %r>' % (self.id, self.password)