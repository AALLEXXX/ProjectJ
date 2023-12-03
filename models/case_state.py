from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from models.database import Base


class CaseState(Base):
    """
    Класс CaseState представляет состояние задачи в базе данных.

    :param id: Уникальный идентификатор состояния задачи.
    :type id: int

    :param case_state_name: Наименование состояния задачи.
    :type case_state_name: str

    :param case: Отношение между CaseState и Case. Позволяет связывать состояние
                 с соответствующими задачами в базе данных.
    """
    __tablename__ = 'case_state'

    id = Column(Integer, primary_key=True)
    case_state_name = Column(String)
    case = relationship('Case')
