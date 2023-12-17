from PySide6.QtWidgets import QWidget
from db.database_worker import Worker
from db.models.case import Case
from ui.qt_base_ui.ui_casewidget.ui_casewidget import Ui_CaseWidget
from PySide6.QtCore import Slot

class CaseWidget(QWidget):
    """
    Класс CaseWidget представляет виджет для отображения и редактирования информации о задаче.

    :param data: Объект Case, представляющий данные о задаче.
    :type data: Case
    """
    def __init__(self, data: Case, worker: Worker=None, case_list= None,
                 status_case = '', author_name = ''):
        """
        Инициализирует экземпляр класса CaseWidget.

        :param data: Объект Case, представляющий данные о задаче.
        :type data: Case
        """
        super(CaseWidget, self).__init__()
        self.ui = Ui_CaseWidget()
        self.ui.setupUi(self)
        self.ui.targetEdit.setText(data.target)
        self.ui.descriptionEdit.setPlainText(data.description)
        self.data = data
        self.worker = worker
        self.case_list = case_list
        self.__set_status_label(status_case)
        self.ui.author_case.setText(f'Автор: {author_name}')
        self.ui.targetEdit.editingFinished.connect(self.editingFinished)
        self.ui.descriptionEdit.textChanged.connect(self.descriptionChanged)
        self.ui.clear_but.clicked.connect(self.delete_case_widget)

    def __set_status_label(self, status_case):
        if status_case.lower().strip() == 'критическая' or status_case.lower().strip() == 'блокирующая':
            self.setStyleSheet('background-color: rgb(255, 0, 0); border-radius: 5px;')
        self.ui.status_case.setText(f'Задача: {status_case.lower()}')
    def delete_case_widget(self):
        id = self.data.id
        self.worker.deleteCase(id)
        self.case_list.listWidget.clear()
        self.case_list.update_widget()


    @Slot()
    def editingFinished(self):
        """
        Слот, вызываемый при завершении редактирования поля 'Цель'.
        Обновляет данные о цели задачи в объекте Case.
        """
        self.data.target = self.ui.targetEdit.text()
        self.worker.save_data()
    @Slot()
    def descriptionChanged(self):
        """
        Слот, вызываемый при изменении текста в поле 'Описание'.
        Обновляет данные об описании задачи в объекте Case.
        """
        desc = self.ui.descriptionEdit.toPlainText()
        self.data.description = desc
        self.worker.save_data()


