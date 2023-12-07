import re

from ui.qt_base_ui.ui_reg_win.ui_create_acc_window import Ui_Dialog
from PySide6.QtWidgets import QDialog


class Registration_window(QDialog):
    def __init__(self, worker):
        super(Registration_window, self).__init__()
        self.worker = worker
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(640, 500)
        self.ui.create_acc_but.clicked.connect(self.create_acc_but_clicked)

    def create_acc_but_clicked(self):
        login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        name = self.ui.name_line.text()
        if len(login) < 4 or not re.match(r'^\S+$', login):
            print('Некорректный логин. Логин не должен содержать пробелов или специальных символов.')
        elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{4,}$', password):
            print('Некорректный пароль. Пароль должен содержать как минимум одну букву и одну цифру, и быть не менее 4 символов в длину.')
        elif len(name) < 2:
            print('короткое имя')
        else:
            if self.worker.registration(login=login, password=password, name=name):
                self.accept()
            else:
                print('Такой логин уже зарегистрирован')


