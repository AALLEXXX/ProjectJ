from PySide6.QtWidgets import QDialog

from db.database_worker import Worker
from ui.create_acc_window import Prog_registration_window
from ui.create_lead_acc_win import Lead_registration_window
from ui.qt_base_ui.ui_log_win.ui_log_in_window import Ui_Dialog


class Login_window(QDialog):
    def __init__(self, worker: Worker):
        super(Login_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.worker = worker
        self.ui.log_in_but.clicked.connect(self.log_in_but)
        self.ui.create_acc_prog_but.clicked.connect(self.create_prog_acc_but_click)
        self.ui.create_acc_lead_but.clicked.connect(self.create_lead_acc_but_click)

    def log_in_but(self):
        login = self.ui.login_text.text()
        password = self.ui.password_text.text()
        user = self.worker.authorization(login=login, password=password)
        if user:
            self.accept()
            return user
        else:
            self.ui.warning_label.setStyleSheet('color:red;')
            self.ui.warning_label.setText('Неверный логин или пароль')

    def create_prog_acc_but_click(self):
        reg_win = Prog_registration_window(self.worker)
        reg_win.exec()

    def create_lead_acc_but_click(self):
        reg_win = Lead_registration_window(self.worker)
        reg_win.exec()
