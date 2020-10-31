# db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'todo'
USERNAME = 'root'
PASSWORD = 'qwe123'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
print(DB_URI)

engine = create_engine(DB_URI)
DBSession = sessionmaker(engine)
Base = declarative_base(engine)
