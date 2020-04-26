import logging

from PyQt5 import QtWidgets, QtCore, QtGui

from ui import PCUwidgets
from ui import PCUicons

logger_pcu_boot = logging.getLogger('pcu_boot_logger')
logger = logging.getLogger(__name__)


class PCUmenuBoot(PCUwidgets.PCUmenu):
    def __init__(self, parent):
        super(PCUmenuBoot, self).__init__(parent)

        self.boot_terminal_message()
        self.init_ui()

    @staticmethod
    def boot_terminal_message():
        message = 'PRODUCTION COMPANION UNIT\n' \
                  '2020 CLEMENTIN MASSIN - https://github.com/ClementinM/ProductionCompanionUnit'
        logger_pcu_boot.info(message)

    def init_ui(self):
        self.setGeometry(0, 0, self.parent.width(), self.parent.height())
        self.setStyleSheet('font-weight: bold;')

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(main_layout)
        main_layout.addStretch()

        init_info_label = QtWidgets.QLabel('PRODUCTION COMPANION UNIT', self)
        main_layout.addWidget(init_info_label)
        init_standby_label = QtWidgets.QLabel('PLEASE STAND BY', self)
        init_standby_label.setStyleSheet('font-size: 24pt;')
        main_layout.addWidget(init_standby_label)

        init_boot_label = QtWidgets.QLabel('INITIATING...', self)
        init_boot_label.setStyleSheet("color: rgba(100, 230, 100, 0.4);")
        main_layout.addWidget(init_boot_label)

        main_layout.addStretch()

    def closing(self):
        self.setParent(None)
        self.close()
