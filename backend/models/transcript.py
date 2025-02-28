from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Transcript(Base):
    __tablename__ = 'transcripts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String) 