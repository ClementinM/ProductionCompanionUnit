from PyQt5 import QtWidgets
from ui import PCUstylesheets


class PCUwindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(PCUwindowMain, self).__init__()
        self.setStyleSheet(PCUstylesheets.get('PCUstylesheetMain'))
        self.setWindowTitle('Production Companion Unit')
        self.setFixedSize(800, 800)

    def closeEvent(self, event):
        print('[wip] APP CLOSING')
