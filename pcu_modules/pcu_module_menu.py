import logging

from ui.pcu_widgets import PCUwidgetMultithread

logger = logging.getLogger(__name__)


class PCUmoduleMenu(PCUwidgetMultithread):
    MODULE_BAR_NAME = ''

    def __init__(self, parent, resize_to_parent=True):
        super(PCUmoduleMenu, self).__init__(parent=parent)
        self.core = None
        self.parent = parent
        self.name = ''
        self.bar_name = ''
        self.bar_button = None

        if resize_to_parent:
            self.resize(self.parent.width(), self.parent.height())

    def load_menu(self):
        pass
