from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Insight(Base):
    __tablename__ = 'insights'
    id = Column(Integer, primary_key=True, index=True)
    transcript_id = Column(Integer, ForeignKey('transcripts.id'))
    key_assumptions = Column(String)
    strategic_direction = Column(String)
    key_disagreements = Column(String)
    unanswered_questions = Column(String) 