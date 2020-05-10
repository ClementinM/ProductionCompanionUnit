import logging

from PyQt5 import QtWidgets, QtCore

logger_pcu_boot = logging.getLogger('pcu_boot_logger')
logger = logging.getLogger(__name__)


class PCUmenuBoot(QtWidgets.QWidget):
    """
    PCU boot menu, displayed during the loading time at the startup.
    """
    def __init__(self, parent):
        """
        :param QWidget parent: ui parent object
        """
        super(PCUmenuBoot, self).__init__(parent)
        self.parent = parent
        self.resize(self.parent.width(), self.parent.height())

        logger_pcu_boot.info(self.boot_terminal_message())
        self.init_ui()

    @staticmethod
    def boot_terminal_message():
        """
        Return boot terminal message, with some info about the app.

        :return message: info message
        :rtype: str
        """
        message = 'PRODUCTION COMPANION UNIT\n' \
                  '2020 CLEMENTIN MASSIN - https://github.com/ClementinM/ProductionCompanionUnit'
        return message

    def init_ui(self):
        """
        Initialize the ui.
        """
        self.setGeometry(0, 0, self.parent.width(), self.parent.height())
        self.setStyleSheet('font-weight: bold;')

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(main_layout)
        main_layout.addStretch()

        init_standby_label = QtWidgets.QLabel('* PLEASE STAND BY *', self)
        init_standby_label.setStyleSheet('font-size: 24pt;')
        main_layout.addWidget(init_standby_label)

        init_boot_label = QtWidgets.QLabel('<center>INITIATING...</center>', self)
        opacity = QtWidgets.QGraphicsOpacityEffect()
        opacity.setOpacity(0.5)
        init_boot_label.setGraphicsEffect(opacity)
        main_layout.addWidget(init_boot_label)

        main_layout.addStretch()

    def closing(self):
        """
        Close this menu.
        """
        self.setParent(None)
        self.close()
