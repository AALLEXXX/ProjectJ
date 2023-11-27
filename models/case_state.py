from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from models.database import Base


class CaseState(Base):
    __tablename__ = 'case_state'

    id = Column(Integer, primary_key=True)
    case_state_name = Column(String)
    case = relationship('Case')
