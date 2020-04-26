from PyQt5 import QtWidgets, QtCore
from .PCUwidgetMultithread import PCUwidgetMultithread


class PCUmenu(PCUwidgetMultithread):
    def __init__(self, parent, resize_to_parent=True):
        super(PCUmenu, self).__init__(parent=parent)
        self.parent = parent

        if resize_to_parent:
            self.resize(self.parent.width(), self.parent.height())

    def set_menu(self):
        self.parent.setCentralWidget(self)

    def load_menu(self):
        pass
