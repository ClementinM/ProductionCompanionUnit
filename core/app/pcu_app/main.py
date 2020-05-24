import logging

import pcu_modules

from .ui import PCUwindowMain
from .. import pcu_environment
from ..pcu_boot import PCUmenuBoot


logger = logging.getLogger(__name__)


class PCUapp(object):
    """
    PCU application core.
    """
    def __init__(self):
        # App main window
        self.pcu_window_main = PCUwindowMain()

        # Init window with boot loading screen
        self.menu_boot = PCUmenuBoot(self.pcu_window_main)
        self.pcu_window_main.show()

        # Setup env
        # TODO: finishing the env setup
        userdatabase = pcu_environment.users.PCUusersDatabase()
        # userdatabase.register_new_user(name_id='cmassin', name_first='clementin', name_last='massin', email='clem.massin@gmail.com')
        pcu_environment.update_user('00000000-0000-0000-0000-000000000000')

        # Init PCU modules
        self.modules = [
            pcu_modules.PCUmodule(pcu_modules.pcu_module_welcome, self.pcu_window_main),
        ]

        # Load PCU modules
        logger.info('Loading PCU modules...')
        self.len_modules_loaded = 0
        self.load_modules()

    def load_modules(self):
        """
        Load every pcu_modules.
        """
        for module in self.modules:
            logger.info('    Loading {} v{}'.format(module.name, module.version))
            module_ui = module.ui
            self.pcu_window_main.add_to_module_bar(module_ui)
            module_ui.separate_thread(module_ui.load_menu, func_finished=self.load_module_finished)

    def load_module_finished(self):
        """
        Function executed after the end of the loading of each pcu_module.
        If every pcu_modules are loaded, it init the default menu to be displayed.
        """
        self.len_modules_loaded += 1
        if self.len_modules_loaded >= len(self.modules):
            logger.info('All PCU modules loaded.')
            self.menu_boot.closing()

            self.pcu_window_main.init_ui()
            self.pcu_window_main.set_current_module(self.modules[0].ui)
