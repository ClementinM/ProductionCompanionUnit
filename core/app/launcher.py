import logging
import sys

from PyQt5 import QtWidgets

from core.app import PCUapp
from core.app import PCUlogging

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    PCUlogging.setup_loggers()

    app = QtWidgets.QApplication(sys.argv)
    pcu_app = PCUapp.PCUapp()
    app.exec_()
