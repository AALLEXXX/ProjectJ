from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base, Session


class Case(Base):
    """
    Класс Case представляет модель данных для задачи в базе данных.

    :param id_case_state: Идентификатор состояния задачи, связанный с ForeignKey 'case_state.id'.
    :type id_case_state: int

    :param target: Цель задачи.
    :type target: str

    :param description: Описание задачи.
    :type description: str
    """
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    target = Column(String)
    description = Column(String)
    team_code = Column(String, ForeignKey('leads.team_code'))
    case_state = Column(Integer, ForeignKey('case_state.id'))
    status_case = Column(String)
    author_case = Column(String)
    lead = relationship('Lead', back_populates='cases')

    def __init__(self, id_case_state: int, target: str = None, description: str = None,
                 team_code: str = '', status_case: str = '', author_case: str = ''):
        self.target = target
        self.description = description
        self.case_state = id_case_state
        self.team_code = team_code
        self.status_case = status_case
        self.author_case = author_case

    def update_state(self):
        """
        Обновляет состояние задачи в базе данных.
        """
        session = Session()  # TODO
        session.query(Case).filter(Case.id == self.id).update({Case.case_state: self.case_state})
        session.commit()

    def update_data(self, session):
        """
        Обновляет данные задачи в базе данных.

        :param session: Сеанс SQLAlchemy для выполнения запросов.
        :type session: Session
        """
        session.query(Case).filter(Case.id == self.id).update({Case.target: self.target,
                                                               Case.description: self.description})
        # session.commit()

    def __repr__(self):
        return f'Дело [{self.target} ID: {self.id}, state: {self.case_state}]'
