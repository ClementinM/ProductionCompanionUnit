import logging

from PyQt5 import QtWidgets
from ui import pcu_stylesheets

logger = logging.getLogger(__name__)


class PCUwindowMain(QtWidgets.QMainWindow):
    """
    PCU application main window.
    """
    def __init__(self):
        super(PCUwindowMain, self).__init__()

        self.setStyleSheet(pcu_stylesheets.get('main'))
        self.setWindowTitle('PCU - Production Companion Unit')
        self.setFixedSize(800, 800)

        # init class variables
        self.current_module = None
        self.current_module_style = 'background-color: rgba(220, 230, 220, 0.3);'

        # init central widget and layout
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setVisible(False)
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_widget.setLayout(self.central_layout)

        # HEADER: module menur bar
        self.module_bar = QtWidgets.QHBoxLayout()
        self.central_layout.addLayout(self.module_bar)

        # CORE: module area
        self.module_layout = QtWidgets.QVBoxLayout()
        self.central_layout.addLayout(self.module_layout)
        self.central_layout.addStretch()

    def init_ui(self):
        """
        Initialize and show the ui.
        """
        self.module_bar.addStretch()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setVisible(True)

    def add_to_module_bar(self, module_ui):
        """
        Add the given pcu_module ui to the pcu_module bar list of the app.

        :param PCUmoduleMenu module_ui: pcu_module ui object.
        """
        module_button = QtWidgets.QPushButton('[ {} ]'.format(module_ui.MODULE_BAR_NAME.upper()), self)
        module_ui.bar_button = module_button
        module_button.clicked.connect(lambda: self.set_current_module(module_ui))
        self.module_bar.addWidget(module_button)

    def set_current_module(self, module_ui):
        """
        Set the given module ui as the current module in use in the app.

        :param PCUmoduleMenu module_ui: pcu_module ui object.
        """
        if self.current_module:
            if module_ui == self.current_module:
                return
            self.current_module.bar_button.setStyleSheet(self.styleSheet())
            self.current_module.setParent(None)
        self.current_module = module_ui
        self.current_module.bar_button.setStyleSheet(self.current_module_style)
        self.current_module.setParent(self)
        self.module_layout.addWidget(self.current_module)

    def closeEvent(self, event):
        """
        App closing event.

        :param QCloseEvent event: closing event
        """
        print('[wip] APP CLOSING')
