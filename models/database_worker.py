from models.case_state import CaseState
from models.case import Case
from models.database import create_db, Session


def create_database():
    create_db()
    session = Session()
    session.add(CaseState(case_state_name='Идея'))
    session.add(CaseState(case_state_name='В процессе'))
    session.add(CaseState(case_state_name='Готово'))
    session.commit()
    session.close()


class Worker:

    def __init__(self, session: Session):
        self.session = session

    def createCase(self, state: CaseState) -> Case:
        case = Case(state.id)
        self.session.add(case)
        self.session.commit()
        return case

    def getStates(self) -> list[CaseState]:
        return [it for it in self.session.query(CaseState)]

    def getCases(self, state: CaseState) -> list[Case]:
        return [it for it in self.session.query(Case).filter(Case.case_state == state.id)]

    def deleteCases(self, state: CaseState) -> None:
        self.session.query(Case).filter(Case.case_state == state.id).delete(synchronize_session='fetch')

    def __del__(self):
        for it in self.session.query(Case):
            it.update_data(self.session)
        self.session.commit()
        self.session.close()

















