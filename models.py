from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)
    
    history = relationship("History", back_populates="user")

class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    input_text = Column(String)
    output_text = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="history")
