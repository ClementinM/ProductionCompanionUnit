import os

current_dir = os.path.dirname(__file__)


def get(stylesheet_name):
    """
    Get the file content of the given stylesheet file name.

    :param str stylesheet_name: stylesheet file name, without extension
    :return: stylesheet file opened and read
    :rtype: str
    """
    stylesheet_filepath = os.path.join(current_dir, '{0}.css'.format(stylesheet_name))
    return open(stylesheet_filepath).read()
