import logging
import time

from PyQt5 import QtWidgets, QtCore

from core.app import PCUboot
from ui import PCUwidgets

logger = logging.getLogger(__name__)


class PCUmenuMain(PCUwidgets.PCUmenu):
    def __init__(self, parent):
        super(PCUmenuMain, self).__init__(parent=parent)
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

    def load_module(self):
        self.load_menu()

    def load_menu(self):
        time.sleep(2)


class PCUapp(object):
    def __init__(self):
        self.window_main = PCUwidgets.PCUwindowMain()

        # Init window with boot loading screen
        self.menu_boot = PCUboot.PCUmenuBoot(self.window_main)
        self.menu_boot.set_menu()
        self.window_main.show()

        logger.info('Loading modules...')
        self.modules = []
        self.len_modules_loaded = 0

        # LOADING CORE MODULES
        # TODO: setup user loggin
        # TODO: setup env

        # LOADING MODULES
        # TODO: modules (:

        # LOADING MAIN MENU
        self.menu_main = PCUmenuMain(self.window_main)
        self.load_module(self.menu_main)

    def load_module(self, module):
        self.modules.append(module)
        module.separate_thread(module.load_module, func_finished=self.set_default_menu)

    def set_default_menu(self):
        self.len_modules_loaded += 1
        if self.len_modules_loaded >= len(self.modules):
            logger.info('All modules loaded!')
            self.menu_main.set_menu()
            self.menu_boot.closing()
