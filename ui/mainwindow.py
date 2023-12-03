import PySide6
from PySide6.QtWidgets import QMainWindow

from models.database_worker import Worker
from ui.qt_base_ui.ui_mainwindow import Ui_MainWindow
from ui.caselistwidget import CaseListWidget
from PySide6.QtGui import QCloseEvent


class MainWindow(QMainWindow):
    """
    Класс MainWindow представляет главное окно приложения.
    """
    def __init__(self, worker: Worker):
        """
        Инициализирует экземпляр класса MainWindow.

        :param worker: Объект Worker.
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = worker
        for it in worker.getStates():
            self.ui.todoListLayout.addWidget(CaseListWidget(it, worker))

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        del self.worker
