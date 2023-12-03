import os
import sys

from PySide6.QtWidgets import QApplication
from models.database import Session, engin
from models.database_worker import  Worker
from ui.mainwindow import MainWindow
from sqlalchemy_utils import database_exists
from models.database_worker import create_database


if __name__ == '__main__':
    """
    entry point
    """
    if not database_exists(engin.url):
        create_database()
        from models.database_worker import create_tables
        create_tables()

    app = QApplication()
    window = MainWindow(Worker(Session()))
    window.setWindowTitle('Alexandria')
    window.setFixedSize(1280, 720)
    window.show()
    sys.exit(app.exec())


