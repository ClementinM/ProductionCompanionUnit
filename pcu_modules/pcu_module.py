import logging

logger = logging.getLogger(__name__)


class PCUmodule(object):
    """
    PCU module object: main wrapper class for each pcu_module.
    """
    def __init__(self, module_object, ui_parent):
        """
        :param module module_object: python module object of the pcu_module
        :param QWidget ui_parent: ui parent object, the ui of the pcu_module will be parented to it
        """
        self.module_object = module_object
        self.name = self.module_object.__name__
        self.version = self.module_object.__version__
        self.core = self.module_object.ModuleCore()
        self.ui = self.module_object.ModuleUi(self.core, ui_parent)
