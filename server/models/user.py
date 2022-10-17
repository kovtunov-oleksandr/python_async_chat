from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    nickname = Column(String, primary_key=True, unique=True)
    password = Column(String)
    email = Column(String, nullable=True)



