from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import postgresql as settings


def get_engin(user, passwd, host, db):
    url = f'postgresql+psycopg2://{user}:{passwd}@{host}/{db}'
    engin = create_engine(url, echo=False)
    return engin


def get_engin_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')
    return get_engin(settings['pguser'],
                     settings['pgpasswd'],
                     settings['pghost'],
                     settings['pgdb'])


engin = get_engin_from_settings()


def get_session():
    engin = get_engin_from_settings()
    session = sessionmaker(bind=engin, expire_on_commit=False)
    return session


Session = get_session()

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engin)
