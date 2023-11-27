from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget, QAbstractItemView, QListWidgetItem, QListWidget

from models.database_worker import Worker
from models.case import Case
from models.case_state import CaseState
from ui.qt_base_ui.ui_todolist import Ui_ToDoListWidget
from ui.casewidget import CaseWidget


class MyListWidget(QListWidget):

    def __init__(self, id_state: int, parent=None):
        super(MyListWidget, self).__init__(parent)
        self.id_state = id_state
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.model().rowsInserted.connect(self.handleRowsInserted, Qt.QueuedConnection)

    def handleRowsInserted(self, parent, first, last):
        for it in range(first, last + 1):
            item = self.item(it)
            if item is not None and self.itemWidget(item) is None:
                data = item.data(Qt.UserRole)
                if data.case_state != self.id_state:
                    data.case_state = self.id_state
                    data.update_state()
                widget = CaseWidget(data)
                item.setSizeHint(widget.sizeHint())
                self.setItemWidget(item, widget)


class CaseListWidget(QWidget):

    def __init__(self, case_state: CaseState, worker: Worker):
        super(CaseListWidget, self).__init__()
        self.ui = Ui_ToDoListWidget()
        self.ui.setupUi(self)
        self.case_state = case_state
        self.worker = worker
        self.ui.groupBox.setTitle(case_state.case_state_name)
        self.ui.addButton.clicked.connect(self.add_widget)
        self.ui.clearButton.clicked.connect(self.clear_widget_list)
        self.listWidget = MyListWidget(self.case_state.id, self)
        self.ui.todoListLayout.addWidget(self.listWidget)
        for it in self.worker.getCases(case_state):
            self._add_widget(it)

    def _add_widget(self, case: Case):
        my_item = QListWidgetItem(self.listWidget)
        my_item.setData(Qt.UserRole, case)
        self.listWidget.addItem(my_item)

    @Slot()
    def add_widget(self):
        self._add_widget(self.worker.createCase(self.case_state))

    @Slot()
    def clear_widget_list(self):
        self.worker.deleteCases(self.case_state)
        self.listWidget.clear()














