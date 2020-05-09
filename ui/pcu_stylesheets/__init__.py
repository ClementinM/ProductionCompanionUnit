import os

current_dir = os.path.dirname(__file__)


def get(stylesheet_name):
    stylesheet_filepath = os.path.join(current_dir, '{0}.css'.format(stylesheet_name))
    return open(stylesheet_filepath).read()
