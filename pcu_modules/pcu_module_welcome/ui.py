import logging

from PyQt5 import QtWidgets, QtCore

from .. import PCUmoduleMenu
from core.app import pcu_environment

logger = logging.getLogger(__name__)


class PCUmoduleWelcomeUi(PCUmoduleMenu):
    """
    PCU module main menu.
    """
    MODULE_BAR_NAME = 'Welcome'

    def __init__(self, core, parent):
        """
        :param class core: logic core class of the pcu_module
        :param QWidget parent: ui parent object
        """
        super(PCUmoduleWelcomeUi, self).__init__(core=core, parent=parent)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(main_layout)

        current_user = pcu_environment.user()

        message = 'Welcome {}!\n\n\n' \
                  'PRODUCTION COMPANION UNIT - 2020 CLEMENTIN MASSIN\n' \
                  'https://github.com/ClementinM/ProductionCompanionUnit'.format(current_user.name_full.title())

        self.tmp_widget = QtWidgets.QLabel(message, self)
        self.tmp_widget.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        main_layout.addWidget(self.tmp_widget)
