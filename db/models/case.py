from sqlalchemy import Integer, Column, String, ForeignKey

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
    user_id = Column(Integer, ForeignKey('users.id') )
    case_state = Column(Integer, ForeignKey('case_state.id'))

    def __init__(self, id_case_state: int, target:str = "", description:str = "", user_id: int=1):
        self.target = target
        self.description = description
        self.case_state = id_case_state
        self.user_id = user_id

    def update_state(self):
        """
        Обновляет состояние задачи в базе данных.
        """
        session = Session() #TODO
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