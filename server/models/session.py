from sqlalchemy import String, Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from server.models.user import Base


class UserSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    token = Column(String)

    user = relationship("User", backref="user_sessions")
