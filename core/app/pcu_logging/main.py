import logging


def set_global_logger():
    """ Set the global logger for the whole app. """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s',
                        datefmt='%H:%M:%S')


def set_boot_logger():
    """ Set the boot logger (only to display boot messages). """
    logger = logging.getLogger('pcu_boot_logger')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def pcu_logger_setup():
    """ Main: app logging setup. """
    set_global_logger()
    set_boot_logger()
