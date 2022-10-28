from sqlalchemy import Column, Integer
from sqlalchemy import String
from server.models.user import Base


class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True)
    chat_name = Column(String, unique=True)
    creator_id = Column(Integer)
    type = Column(Integer)