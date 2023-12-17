from PySide6.QtWidgets import QDialog

from ui.qt_base_ui.ui_text_widget.ui_text_window import Ui_Form


class ExtraWindow(QDialog):  # TODO рефактор
    def __init__(self, worker):
        super(ExtraWindow, self).__init__()
        self.worker = worker
        self.status_case = None
        self.ui_extra_window = Ui_Form()
        self.ui_extra_window.setupUi(self)
        self.ui_extra_window.create_case_but.clicked.connect(self.create_case_button)
        self.ui_extra_window.buttonGroup.buttonClicked.connect(self.lvl_but_click)

    def create_case_button(self):
        if len(self.ui_extra_window.target_TextEdit.toPlainText()) > 2 and \
                len(self.ui_extra_window.descr_TextEdit.toPlainText()) > 2 and \
                self.status_case != None:
            self.close()

    def get_data(self) -> dict:
        if len(self.ui_extra_window.target_TextEdit.toPlainText()) > 2 and \
                len(self.ui_extra_window.descr_TextEdit.toPlainText()) > 2 and \
                self.status_case != None:
            data = {'target': self.ui_extra_window.target_TextEdit.toPlainText(),
                    'description': self.ui_extra_window.descr_TextEdit.toPlainText(),
                    'status_case': self.status_case}
            return data if data else None

    def lvl_but_click(self, button):
        lvl = button.text()
        self.status_case = lvl
