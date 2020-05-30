import logging

from PyQt5 import QtWidgets

logger = logging.getLogger(__name__)


class UserRegisterUi(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UserRegisterUi, self).__init__(parent=parent)
