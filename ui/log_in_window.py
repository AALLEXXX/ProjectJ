from PySide6.QtWidgets import QDialog

from db.database_worker import Worker
from ui.create_acc_window import Registration_window
from ui.qt_base_ui.ui_log_win.ui_log_in_window import Ui_Dialog
class Login_window(QDialog):
    def __init__(self, worker: Worker):
        super(Login_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.worker = worker
        self.setFixedSize(640, 500)
        self.ui.log_in_but.clicked.connect(self.log_in_but)
        self.ui.create_acc_but.clicked.connect(self.create_acc_but)

    def log_in_but(self):
        login = self.ui.login_text.text()
        password = self.ui.password_text.text()
        user = self.worker.authorization(login=login,password=password)
        if user:
            self.accept()
            return user
        else:
            print('неверный логин или пароль') #TODO

    def create_acc_but(self):
        reg_win = Registration_window(self.worker)
        reg_win.exec()

