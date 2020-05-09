from PyQt5 import QtWidgets, QtCore


class QWidgetThread(QtCore.QThread):
    sig_start = QtCore.pyqtSignal()
    sig_finished = QtCore.pyqtSignal()

    def __init__(self, parent=None, func=None):
        super(QWidgetThread, self).__init__(parent=parent)
        self.parent = parent
        self.function_to_run = func

    def run(self):
        self.sig_start.emit()
        if self.function_to_run:
            self.function_to_run()
        self.sig_finished.emit()


class PCUwidgetMultithread(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PCUwidgetMultithread, self).__init__(parent=parent)
        self.parent = parent
        self.menu_thread = None

    def separate_thread(self, func, func_start=None, func_finished=None):
        self.menu_thread = QWidgetThread(self, func=func)
        if func_start:
            self.menu_thread.sig_start.connect(func_start)
        if func_finished:
            self.menu_thread.sig_finished.connect(func_finished)
        self.menu_thread.start()
