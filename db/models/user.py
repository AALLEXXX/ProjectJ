from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    programming_lvl = Column(String)
    lead_id = Column(Integer, ForeignKey('leads.id'))  # Внешний ключ, связывающий с таблицей leads
    lead = relationship('Lead', back_populates='users')

    def __init__(self, login: str, password: str, name: str, programming_lvl: str, lead_id: int):
        self.lead_id = lead_id
        self.programming_lvl = programming_lvl
        self.login = login
        self.password = password
        self.name = name
