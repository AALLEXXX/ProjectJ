from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from db.models.case import Case
from ui.qt_base_ui.ui_casewidget import Ui_CaseWidget


class CaseWidget(QWidget):
    """
    Класс CaseWidget представляет виджет для отображения и редактирования информации о задаче.

    :param data: Объект Case, представляющий данные о задаче.
    :type data: Case
    """
    def __init__(self, data: Case):
        """
        Инициализирует экземпляр класса CaseWidget.

        :param data: Объект Case, представляющий данные о задаче.
        :type data: Case
        """
        super(CaseWidget, self).__init__()
        self.ui = Ui_CaseWidget()
        self.ui.setupUi(self)
        self.ui.targetEdit.setText(data.target)
        self.ui.descriptionEdit.setText(data.description)
        self.data = data
        self.ui.targetEdit.editingFinished.connect(self.editingFinished)
        self.ui.descriptionEdit.textChanged.connect(self.descriptionChanged)

    @Slot()
    def editingFinished(self):
        """
        Слот, вызываемый при завершении редактирования поля 'Цель'.
        Обновляет данные о цели задачи в объекте Case.
        """
        self.data.target = self.ui.targetEdit.text()

    @Slot()
    def descriptionChanged(self):
        """
        Слот, вызываемый при изменении текста в поле 'Описание'.
        Обновляет данные об описании задачи в объекте Case.
        """

        self.data.description = self.ui.descriptionEdit.toPlainText()
