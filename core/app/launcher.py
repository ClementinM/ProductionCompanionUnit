import logging
import sys

from PyQt5 import QtWidgets

from core.app.pcu_app import PCUapp
from core.app.pcu_logging import pcu_logger_setup

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    pcu_logger_setup()

    app = QtWidgets.QApplication(sys.argv)
    pcu_app = PCUapp()
    app.exec_()
