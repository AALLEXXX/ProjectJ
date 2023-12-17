import re

from ui.qt_base_ui.ui_reg_wins.reg_prog.ui_create_acc_window import Ui_Dialog
from PySide6.QtWidgets import QDialog


def validate_login(login):
    return re.match(r'^[a-zA-Z0-9]+$', login.strip().lower())

def validate_password(password):
    return re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{4,}$', password.strip())

def validate_name(name):
    return 2 <= len(name.strip()) <= 10

def validate_code(code):
    return len(code.strip()) == 4

def validate_lead_id(lead_id):
    return lead_id is not None


class Prog_registration_window(QDialog):
    def __init__(self, worker):
        super(Prog_registration_window, self).__init__()
        self.worker = worker
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.lvl_prog = None
        self.ui.create_acc_but.clicked.connect(self.create_acc_but_clicked)
        self.ui.buttonGroup.buttonClicked.connect(self.lvl_prog_click)
        self.ui.warning_label.setStyleSheet('color:orange;')

    def create_acc_but_clicked(self):
        login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        name = self.ui.name_line.text()
        prog_lvl = self.lvl_prog
        code = self.ui.code_line.text()
        lead_id = self.worker.get_lead_id(code)
        if any(value is '' for value in (login, password, name, code)) or prog_lvl is None:
            self.show_warning('Заполните все поля')
        elif not validate_login(login):
            self.show_warning('Логин должен содержать только латинские буквы и цифры')
        elif not (4 <= len(login.strip()) <= 10):
            self.show_warning('Длина логина должна быть от 4 до 10 символов')
        elif not validate_password(password):
            self.show_warning(
                'Пароль должен содержать как минимум одну букву латинского алфавита и одну цифру, и быть не менее 4 символов в длину.')
        elif not validate_name(name):
            self.show_warning('Допустимая длина имени от 2 до 10 символов.')
        elif not validate_code(code):
            self.show_warning('Некорректная длина кода')
        elif not validate_lead_id(lead_id):
            self.show_warning('Команды с таким кодом не найдено')
        else:
            reg = self.worker.programmer_registration(login=login, password=password, name=name, lvl_prog=prog_lvl,
                                                      lead_id=lead_id)
            if reg:
                self.accept()
            else:
                self.show_warning('Такой логин уже зарегистрирован')

    def show_warning(self, message):
        self.ui.warning_label.setText(message)
    def lvl_prog_click(self, button):
        lvl_dict = {'Мидл': 'middle',
                    'Сеньор': 'senior',
                    'Джуниор': 'junior'}
        result = lvl_dict.get(button.text())
        self.lvl_prog = result
