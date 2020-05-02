import logging

import pcumodules

from .PCUwindowMain import PCUwindowMain
from core.app import PCUboot

logger = logging.getLogger(__name__)


class PCUapp(object):
    def __init__(self):
        self.window_main = PCUwindowMain()

        # Init window with boot loading screen
        self.menu_boot = PCUboot.PCUmenuBoot(self.window_main)
        self.window_main.show()

        # INIT CORE MODULES
        # TODO: setup user loggin
        # TODO: setup env

        # INIT MODULES
        self.module_main = pcumodules.PCUmoduleMain(self.window_main)
        # TODO: modules (:

        # START LOADING MODULES
        logger.info('Loading modules...')
        self.modules = [self.module_main]
        self.len_modules_loaded = 0
        self.load_modules()

    def load_modules(self):
        for module in self.modules:
            logger.info('    Loading {}...'.format(module.name))
            self.window_main.add_to_module_bar(module)
            module.separate_thread(module.load_menu, func_finished=self.load_module_finished)

    def load_module_finished(self):
        self.len_modules_loaded += 1
        if self.len_modules_loaded >= len(self.modules):
            logger.info('All modules loaded!')
            self.menu_boot.closing()

            self.window_main.init_ui()
            self.window_main.set_current_module(self.module_main)

