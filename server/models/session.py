from sqlalchemy import Column, Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    token = Column(String)


