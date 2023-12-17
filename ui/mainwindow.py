import sys

import PySide6
from PySide6.QtWidgets import QMainWindow, QDialog
from db.database_worker import Worker
from ui.qt_base_ui.ui_mainwindow import Ui_MainWindow
from ui.caselistwidget import CaseListWidget
from PySide6.QtGui import QCloseEvent
from ui.log_in_window import Login_window

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
        self.process_authorization()
    def process_authorization(self):
        login_window = Login_window(self.worker)
        result = login_window.exec_()
        if result == QDialog.Accepted:
            self.user = login_window.log_in_but()
            self.ui.pushButton.setText(self.user.name)
            self.show()
            for it in self.worker.getStates():
                self.ui.todoListLayout.addWidget(CaseListWidget(it, self.worker, user=self.user))
        elif result == QDialog.Rejected:
            sys.exit(0)


    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        self.worker.save_data()
        self.worker.session.close()
