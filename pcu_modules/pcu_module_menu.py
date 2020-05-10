import logging

from ui.pcu_widgets import PCUwidgetMultithread

logger = logging.getLogger(__name__)


class PCUmoduleMenu(PCUwidgetMultithread):
    """
    PCU module UI: ui main menu of the pcu_module object.
    """
    # To override: name of the menu displayed in the menu list
    MODULE_BAR_NAME = ''

    def __init__(self, core, parent, resize_to_parent=True):
        """
        :param class core: logic core class of the pcu_module
        :param QWidget parent: ui parent object
        :param bool resize_to_parent: resize the menu to the parent size, or not
        """
        super(PCUmoduleMenu, self).__init__(parent=parent)
        self.parent = parent
        self.core = core
        self.bar_button = None

        if resize_to_parent:
            self.resize(self.parent.width(), self.parent.height())

    def load_menu(self):
        """
        To override: loading menu function. It will be executed in a separated thread.
        """
        pass
