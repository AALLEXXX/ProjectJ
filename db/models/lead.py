from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    team_code = Column(String, unique=True, nullable=False)
    users = relationship('User', back_populates='lead')
    cases = relationship('Case', back_populates='lead')

    def __init__(self, login, password, name, team_code):
        self.login = login
        self.password = password
        self.name = name
        self.team_code = team_code
