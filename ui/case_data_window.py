from PySide6.QtWidgets import QDialog

from ui.qt_base_ui.ui_text_window import Ui_Form


class ExtraWindow(QDialog): #TODO рефактор
    def __init__(self):
        super(ExtraWindow, self).__init__()
        self.ui_extra_window = Ui_Form()
        self.ui_extra_window.setupUi(self)
        self.setFixedSize(400, 300)
        self.ui_extra_window.pushButton.clicked.connect(self.closed_button)

    def closed_button(self):
        self.close()

    def get_data(self) -> dict:
        data = {'target': self.ui_extra_window.target.toPlainText(),
                'description': self.ui_extra_window.descr.toPlainText()}
        return data
