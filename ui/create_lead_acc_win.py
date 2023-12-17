import re
import random
import string
from ui.qt_base_ui.ui_reg_wins.reg_lead.ui_create_acc_lead_window import Ui_Dialog
from PySide6.QtWidgets import QDialog


def generate_code():
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(4))
    return random_word


class Lead_registration_window(QDialog):
    def __init__(self, worker):
        super(Lead_registration_window, self).__init__()
        self.worker = worker
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.create_acc_but.clicked.connect(self.create_acc_but_clicked)
        self.code = generate_code()
        self.ui.code_label.setText(f'{self.ui.code_label.text()} {self.code.upper()}')
        self.ui.warning_label.setWordWrap(True)
        self.ui.warning_label.setStyleSheet('color:;')

    def create_acc_but_clicked(self):
        login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        name = self.ui.name_line.text()
        if any(value is '' for value in (login, password, name)):
            self.show_warning('Заполните все поля')
        elif len(login) < 4 or not re.match(r'^[a-zA-Z0-9]+$', login.strip()):
            self.show_warning('Некорректный логин. Логин не должен содержать пробелов или специальных символов.')
        elif not re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{4,}$', password):
            self.show_warning(
                'Некорректный пароль. Пароль должен содержать как минимум одну букву и одну цифру, и быть '
                'не менее 4 символов в длину.')
        elif len(name) < 2:
            self.show_warning('Короткое имя пользователя')
        else:
            if self.worker.lead_registration(login=login, password=password, name=name, code=self.code):
                self.accept()
            else:
                self.show_warning('Такой логин уже зарегистрирован')

    def show_warning(self, text):
        self.ui.warning_label.setText(text)
