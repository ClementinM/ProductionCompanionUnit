import logging
import time

from PyQt5 import QtWidgets, QtCore

from ui import PCUwidgets

logger = logging.getLogger(__name__)


class PCUmoduleMain(PCUwidgets.PCUmenu):
    def __init__(self, parent):
        super(PCUmoduleMain, self).__init__(parent=parent)
        self.name = 'Main'
        self.module_bar_name = 'Main'

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(main_layout)

        message = 'Welcome!\n\n\n' \
                  'PRODUCTION COMPANION UNIT - 2020 CLEMENTIN MASSIN\n' \
                  'https://github.com/ClementinM/ProductionCompanionUnit'

        self.tmp_widget = QtWidgets.QLabel(message, self)
        self.tmp_widget.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        main_layout.addWidget(self.tmp_widget)

