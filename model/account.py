# account.py


from sqlalchemy import Column, Integer, String, DateTime

from .db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return "name:{}, password{}".format(self.name, self.password)

