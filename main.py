import sys

from PySide6.QtWidgets import QApplication
from db.database import engin
from sqlalchemy_utils import database_exists
from db.database_worker import create_database
from movie_splash import start_splash
from db.database import Session
from db.database_worker import Worker
from ui.mainwindow import MainWindow


if __name__ == '__main__':
    """
    entry point
    """
    if not database_exists(engin.url):
        create_database()
        from db.database_worker import create_tables
        create_tables()

    app = QApplication()
    # start_splash(app, timer=20)
    window = MainWindow(Worker(Session()))
    window.setWindowTitle('Alexandria')
    window.setFixedSize(1400, 800)
    sys.exit(app.exec())


