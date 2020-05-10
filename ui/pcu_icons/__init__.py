import os

current_dir = os.path.dirname(__file__)


def get(icon_name):
    """
    Get the icon file path of the given icon name.

    :param str icon_name: icon file name, with extension
    :return: icon file path
    :rtype: str
    """
    return os.path.join(current_dir, icon_name)
