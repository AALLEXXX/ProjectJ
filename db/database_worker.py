from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db.models.case_state import CaseState
from db.models.case import Case
from db.database import create_db, Session
from db.models.lead import Lead
from db.models.user import User
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tables():
    create_db()
    session = Session()
    session.add(CaseState(case_state_name='Идея'))
    # session.add(CaseState(case_state_name='Личные таски'))
    session.add(CaseState(case_state_name='В процессе'))
    session.add(CaseState(case_state_name='Готово'))
    session.commit()
    session.close()


def create_database():
    connection = psycopg2.connect(user="postgres", password="postgres")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE "projectJ"')
    cursor.close()
    connection.close()


class Worker:
    """
    Класс Worker представляет собой интерфейс для взаимодействия с базой данных,
    осуществляя операции с объектами Case и CaseState.

    :param session: Объект сессии SQLAlchemy, представляющий соединение с базой данных.
    """

    def __init__(self, session: Session):
        """
        Инициализирует экземпляр класса Worker.

        :param session: Объект сессии SQLAlchemy.
        """
        self.session = session

    def createCase(self, state: CaseState, target, description, user: User, status_case) -> Case:
        """
        Создает новый объект Case с указанным состоянием и добавляет его в базу данных.

        :param state: Объект CaseState, представляющий состояние задачи.
        :return: Созданный объект Case.
        """
        team_code = self.get_team_code(user.id)
        case = Case(state.id, target, description, team_code=team_code,
                    status_case=status_case, author_case=user.name)
        self.session.add(case)
        self.session.commit()
        return case

    def getStates(self) -> list[CaseState]:
        """
        Возвращает список всех состояний задач из базы данных.

        :return: Список объектов CaseState.
        """
        return [it for it in self.session.query(CaseState)]

    def getCases(self, state: CaseState, user_id: int) -> list[Case]:
        """
        Возвращает список всех задач с указанным состоянием из базы данных.

        :param state: Объект CaseState, для которого нужно получить задачи.
        :return: Список объектов Case.
        """
        team_code = self.get_team_code(user_id)
        data = [it for it in self.session.
        query(Case).filter(Case.case_state == state.id,
                           Case.team_code == team_code
                           )]
        return data

    def get_team_code(self, user_id):
        user = self.session.query(User).get(user_id)
        try:
            lead = user.lead
            return lead.team_code
        except:
            lead = self.session.query(Lead).get(user_id)
            return lead.team_code


    def deleteCases(self, state: CaseState) -> None:
        """
        Удаляет все задачи с указанным состоянием из базы данных.

        :param state: Объект CaseState, для которого нужно удалить задачи.
        """
        self.session.query(Case).filter(Case.case_state == state.id).delete(synchronize_session='fetch')

    def deleteCase(self, case_id: Case.id):
        case_to_delete = self.session.query(Case).get(case_id)
        if case_to_delete:
            self.session.delete(case_to_delete)
            self.session.commit()
        else:
            print('Not delete')

    def save_data(self):
        for it in self.session.query(Case):
            it: Case
            it.update_data(self.session)
        self.session.commit()

    def authorization(self, login, password):
        user_query = select([User]).where((User.login == login) & (User.password == password))
        lead_query = select([Lead]).where((Lead.login == login) & (Lead.password == password))

        user = self.session.execute(user_query).first()
        if user:
            return user[0]

        lead = self.session.execute(lead_query).first()
        if lead:
            return lead[0]

        return None

    def programmer_registration(self, login, password, name, lvl_prog, lead_id):
        try:
            user = User(login=login, password=password, name=name, programming_lvl=lvl_prog, lead_id=lead_id)
            self.session.add(user)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False

    def get_lead_id(self, code: str) -> Lead.id:
        result = self.session.query(Lead.id).filter(Lead.team_code == code).first()
        return result.id if result else None

    def lead_registration(self, login, password, name, code):
        try:
            lead = Lead(login=login, password=password,
                        name=name, team_code=code)
            self.session.add(lead)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False
