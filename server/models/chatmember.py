
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from server.models.user import Base


class ChatMember(Base):
    __tablename__ = "chat_member"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    chat_id = Column(Integer, ForeignKey('chat.id'))
    permissions = Column(Integer)

    user = relationship("User", backref="chat_member")
    chat = relationship("Chat", backref="chat_member")