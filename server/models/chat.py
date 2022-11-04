from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from server.models.user import Base


class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True)
    chat_name = Column(String, unique=True)
    creator_id = Column(Integer, ForeignKey("users.id"))
    type = Column(Integer)

    user = relationship("User", backref="chat")
