from sqlalchemy.exc import IntegrityError

from db.models.case_state import CaseState
from db.models.case import Case
from db.database import create_db, Session
from db.models.user import User
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tables():
    create_db()
    session = Session()
    session.add(CaseState(case_state_name='Open'))
    session.add(CaseState(case_state_name='Личные таски'))
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

    def createCase(self, state: CaseState, target, description, user_id: int) -> Case:
        """
        Создает новый объект Case с указанным состоянием и добавляет его в базу данных.

        :param state: Объект CaseState, представляющий состояние задачи.
        :return: Созданный объект Case.
        """
        case = Case(state.id, target, description, user_id=user_id)
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
        print(state.id, user_id)
        return [it for it in self.session.
        query(Case).filter(Case.case_state == state.id,
                           Case.user_id == user_id
                           )]

    def deleteCases(self, state: CaseState) -> None:
        """
        Удаляет все задачи с указанным состоянием из базы данных.

        :param state: Объект CaseState, для которого нужно удалить задачи.
        """
        self.session.query(Case).filter(Case.case_state == state.id).delete(synchronize_session='fetch')

    def save_data(self):
        for it in self.session.query(Case):
            it: Case
            it.update_data(self.session)
        self.session.commit()
        self.session.close()

    def authorization(self, login, password):
        user = self.session.query(User).filter_by(login=login, password=password).first()
        self.session.commit()
        return user

    def registration(self, login, password, name):
        try:
            user = User(login=login, password=password, name=name)
            self.session.add(user)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False
