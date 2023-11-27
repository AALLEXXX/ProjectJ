from PySide6.QtWidgets import QWidget

from models.case import Case
from ui.qt_base_ui.ui_casewidget import Ui_CaseWidget


class CaseWidget(QWidget):

    def __init__(self, data: Case):
        super(CaseWidget, self).__init__()
        self.ui = Ui_CaseWidget()
        self.ui.setupUi(self)
        self.ui.targetEdit.setText(data.target)
        self.ui.descriptionEdit.setText(data.description)
        self.data = data
        self.ui.targetEdit.editingFinished.connect(self.editingFinished)
        self.ui.descriptionEdit.textChanged.connect(self.descriptionChanged)

    def editingFinished(self):
        self.data.target = self.ui.targetEdit.text()

    def descriptionChanged(self):
        self.data.description = self.ui.descriptionEdit.toPlainText()
