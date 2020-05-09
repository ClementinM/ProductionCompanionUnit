import logging

logger = logging.getLogger(__name__)


class PCUmodule(object):
    def __init__(self, module_object, ui_parent):
        self.module_object = module_object
        self.name = self.module_object.__name__
        self.version = self.module_object.__version__
        self.core = self.module_object.ModuleCore()
        self.ui = self.module_object.ModuleUi(ui_parent)
