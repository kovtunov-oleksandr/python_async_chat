from sqlalchemy import Column, Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    password = Column(String)
    email = Column(String, nullable=True)

    session = relationship("UserSession", back_populates="user", cascade="all, delete")
    chat_members = relationship("ChatMember", back_populates="user", cascade="all, delete")
