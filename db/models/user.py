from sqlalchemy import Integer, Column, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    case = relationship('Case', cascade='all, delete-orphan')

    def __init__(self, login: str, password: str, name:str):
        self.login = login
        self.password = password
        self.name = name

