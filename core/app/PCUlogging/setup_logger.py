import logging


def set_global_logger():
    # global logging config
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s]: %(message)s',
                        datefmt='%H:%M:%S')


def set_boot_logger():
    # pcu boot logger, only for display boot messages
    logger = logging.getLogger('pcu_boot_logger')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def setup_loggers():
    set_global_logger()
    set_boot_logger()
