from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget, QAbstractItemView, QListWidgetItem, QListWidget
from db.database_worker import Worker
from db.models.case import Case
from db.models.case_state import CaseState
from db.models.user import User
from ui.case_data_window import ExtraWindow
from ui.qt_base_ui.ui_todolist import Ui_ToDoListWidget
from ui.casewidget import CaseWidget


class MyListWidget(QListWidget):
    """
    Класс MyListWidget представляет собой настраиваемый QListWidget с поддержкой
    перетаскивания и связанных с этим дополнительных функций для работы с задачами.

    :param id_state: Уникальный идентификатор состояния задачи, используемый для обновления состояния.
    :type id_state: int

    :param parent: Родительский виджет.
    :type parent: QWidget
    """
    def __init__(self, id_state: int, parent=None):
        """
        Инициализирует экземпляр класса MyListWidget.

        :param id_state: Уникальный идентификатор состояния задачи.
        :type id_state: int

        :param parent: Родительский виджет.
        :type parent: QWidget
        """

        super(MyListWidget, self).__init__(parent)

        self.id_state = id_state
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.model().rowsInserted.connect(self.handleRowsInserted, Qt.QueuedConnection)


    def handleRowsInserted(self, parent, first, last):
        """
        Обработчик события вставки новых строк в список задач.

        :param parent: Родительский индекс.
        :type parent: QModelIndex

        :param first: Индекс первой вставленной строки.
        :type first: int

        :param last: Индекс последней вставленной строки.
        :type last: int
        """
        for it in range(first, last + 1):
            item = self.item(it)
            if item is not None:
                data:Case = item.data(Qt.UserRole)
                if data is not None and data.case_state != self.id_state:
                    data:Case
                    data.case_state = self.id_state
                    data.update_state()
                widget = CaseWidget(data)
                item.setSizeHint(widget.sizeHint())
                self.setItemWidget(item, widget)

class CaseListWidget(QWidget):
    """
    Класс CaseListWidget представляет виджет, отображающий список задач для конкретного состояния.

    :param case_state: Объект CaseState, представляющий состояние задачи.
    :type case_state: CaseState

    :param worker: Объект Worker, предоставляющий интерфейс для работы с базой данных.
    :type worker: Worker
    """
    def __init__(self, case_state: CaseState, worker: Worker, user: User):
        """
        Инициализирует экземпляр класса CaseListWidget.

        :param case_state: Объект CaseState, представляющий состояние задачи.
        :type case_state: CaseState

        :param worker: Объект Worker.
        :type worker: Worker
        """
        super(CaseListWidget, self).__init__()
        self.ui = Ui_ToDoListWidget()
        self.ui.setupUi(self)
        self.case_state = case_state
        self.worker = worker
        self.user = user
        self.ui.groupBox.setTitle(case_state.case_state_name)
        self.ui.addButton.clicked.connect(self.add_widget)
        self.ui.clearButton.clicked.connect(self.clear_widget_list)
        self.listWidget = MyListWidget(self.case_state.id, self)
        self.ui.todoListLayout.addWidget(self.listWidget)
        for it in self.worker.getCases(case_state, self.user.id):
            self._add_widget(it)


    def _add_widget(self, case: Case):
        """
        Добавляет новый виджет задачи в список.

        :param case: Объект Case, представляющий задачу.
        :type case: Case
        """
        my_item = QListWidgetItem(self.listWidget)
        my_item.setData(Qt.UserRole, case)
        self.listWidget.addItem(my_item)

    @Slot()
    def add_widget(self):
        """
        Слот, вызываемый при нажатии кнопки "Добавить". Добавляет новую задачу в список.
        """
        self.dialog_window = ExtraWindow()
        self.dialog_window.exec()
        data = self.dialog_window.get_data()
        target = data['target']
        descr = data['description']
        self._add_widget(self.worker.createCase(self.case_state, target, descr, self.user.id))



    @Slot()
    def clear_widget_list(self):
        """
        Слот, вызываемый при нажатии кнопки "Очистить". Удаляет все задачи из списка.
        """
        self.worker.deleteCases(self.case_state)
        self.listWidget.clear()



