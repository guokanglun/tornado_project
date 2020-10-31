# account.py


from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .db import Base, DBSession


session = DBSession()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "name:{}, password{}".format(self.name, self.password)

    # 插入数据
    @classmethod
    def add_user(cls, username, password):
        user = User(name=username, password=password)
        session.add(user)
        session.commit()

    @classmethod
    def get_password(cls, username):
        user = session.query(cls).filter_by(name=username).first()
        if user:
            return user.password
        else:
            return ''

    @classmethod
    def is_exits(cls,username):
        user = session.query(cls).filter_by(name=username).first()
        return user.name
    
