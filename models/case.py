from sqlalchemy import Integer, Column, String, ForeignKey

from models.database import Base, Session


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    target = Column(String)
    description = Column(String)
    case_state = Column(Integer, ForeignKey('case_state.id'))

    def __init__(self, id_case_state: int, target:str = "", description:str = ""):
        self.target = target
        self.description = description
        self.case_state = id_case_state

    def update_state(self):
        session = Session()
        session.query(Case).filter(Case.id == self.id).update({Case.case_state: self.case_state})
        session.commit()

    def update_data(self, session):
        session.query(Case).filter(Case.id == self.id).update({Case.target: self.target,
                                                               Case.description: self.description})

    def __repr__(self):
        return f'Дело [{self.target} ID: {self.id}, state: {self.case_state}]'