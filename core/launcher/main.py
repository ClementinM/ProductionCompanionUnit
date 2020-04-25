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

"""
##################################


class PCUmenu(QtWidgets.QWidget):
    def __init__(self, parent):
        super(PCUmenu, self).__init__(parent=parent)
        self.parent = parent

    def set_menu(self):
        self.parent.setCentralWidget(self)

    def separate_thread(self, func, func_start=None, func_finished=None):
        menu_thread = PCUmenuThread(self, func=func)
        if func_start:
            menu_thread.sig_start.connect(func_start)
        if func_finished:
            menu_thread.sig_finished.connect(func_finished)
        menu_thread.start()


class PCUmenuThread(QtCore.QThread):
    sig_start = QtCore.pyqtSignal()
    sig_finished = QtCore.pyqtSignal()

    def __init__(self, parent=None, func=None):
        super(PCUmenuThread, self).__init__(parent=parent)
        self.parent = parent
        self.function_to_run = func

    def run(self):
        self.sig_start.emit()
        if self.function_to_run:
            self.function_to_run()
        self.sig_finished.emit()


##################################


class PCUappMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PCUappMainWindow, self).__init__()
        self.setFixedSize(800, 800)

    def closeEvent(self, event):
        # TODO: exit running threads
        print('CLOSING')
        print(event)


class BootMenu(PCUmenu):
    def __init__(self, parent):
        super(BootMenu, self).__init__(parent=parent)
        main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(main_layout)
        boot_widget = QtWidgets.QLabel('loading...........', self)
        main_layout.addWidget(boot_widget)
        print('boot init done')


class SlowMenu(PCUmenu):

    def __init__(self, parent):
        super(SlowMenu, self).__init__(parent=parent)

        main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(main_layout)

        self.slow_widget = QtWidgets.QLabel('BONJOUR', self)
        main_layout.addWidget(self.slow_widget)

        self.separate_thread(func=self.slow_function_1, func_finished=self.set_menu)
        self.separate_thread(func=self.slow_function_2)

    def slow_function_1(self):
        print('SLOW MENU 1: start')
        time.sleep(2)
        print('SLOW MENU 1: stop')

    def slow_function_2(self):
        print('SLOW MENU 2: start')
        time.sleep(4)
        self.slow_widget.setText('GNA')
        print('SLOW MENU 2: stop')


class PCUapp(object):
    def __init__(self):
        self.main_menu = PCUappMainWindow()

        self.boot_menu = BootMenu(self.main_menu)
        self.boot_menu.set_menu()

        self.main_menu.show()

        self.slow_menu = SlowMenu(self.main_menu)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    pcu_application = PCUapp()
    app.exec_()
"""