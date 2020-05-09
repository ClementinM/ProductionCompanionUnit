import logging

import pcu_modules

from .ui import PCUwindowMain
from core.app.pcu_boot import PCUmenuBoot

logger = logging.getLogger(__name__)


class PCUapp(object):
    def __init__(self):
        # App main window
        self.pcu_window_main = PCUwindowMain()

        # Init window with boot loading screen
        self.menu_boot = PCUmenuBoot(self.pcu_window_main)
        self.pcu_window_main.show()

        # Setup env
        # TODO: setup user loggin
        # TODO: setup env

        # Init modules
        self.modules = [
            pcu_modules.PCUmodule(pcu_modules.pcu_module_welcome, self.pcu_window_main),
        ]

        # Load modules
        logger.info('Loading modules...')
        self.len_modules_loaded = 0
        self.load_modules()

    def load_modules(self):
        for module in self.modules:
            logger.info('    Loading {} v{}'.format(module.name, module.version))
            module_ui = module.ui
            self.pcu_window_main.add_to_module_bar(module_ui)
            module_ui.separate_thread(module_ui.load_menu, func_finished=self.load_module_finished)

    def load_module_finished(self):
        self.len_modules_loaded += 1
        if self.len_modules_loaded >= len(self.modules):
            logger.info('All modules loaded.')
            self.menu_boot.closing()

            self.pcu_window_main.init_ui()
            self.pcu_window_main.set_current_module(self.modules[0].ui)
