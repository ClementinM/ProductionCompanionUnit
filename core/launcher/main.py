import logging
import sys
import threading
import time

from PyQt5 import QtWidgets, QtCore

from core.launcher.boot.boot import PCUwindowBoot


def setup_logger():
    # global logging config
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s',
                        datefmt='%H:%M:%S')

    # pcu boot logger, only for display boot messages
    logger = logging.getLogger('logger_pcu_boot')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


class PCUwindowApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(PCUwindowApp, self).__init__()
        self.setStyleSheet(open('./ui/stylesheets/test_stylesheet.css').read())
        self.setWindowTitle('Production Companion Unit')
        self.setFixedSize(800, 800)

        self.pcu_boot = PCUwindowBoot(self)
        self.pcu_boot.show()
        self.pcu_main_menu = PCUwindowMenuMain(self)
        # self.pcu_boot.close()

        self.pcu_main_menu.show()


# TMP MAIN MENU
class PCUwindowMenuMain(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PCUwindowMenuMain, self).__init__(parent=parent)
        self.parent = parent
        # time.sleep(2)
        self.init_ui()
        self.close()

    def init_ui(self):
        self.resize(self.parent.width(), self.parent.height())

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(main_layout)

        buton1 = QtWidgets.QPushButton('INGEST', self)
        buton2 = QtWidgets.QPushButton('DELIVERY', self)
        buton3 = QtWidgets.QPushButton('STAT', self)
        list_butons = [buton1, buton2, buton3]
        for b in list_butons:
            main_layout.addWidget(b)
        main_layout.addStretch()



if __name__ == '__main__':
    setup_logger()
    # TODO: setup user loggin
    # TODO: setup env

    app = QtWidgets.QApplication(sys.argv)
    pcu_window_main = PCUwindowApp()
    pcu_window_main.show()
    app.exec_()
