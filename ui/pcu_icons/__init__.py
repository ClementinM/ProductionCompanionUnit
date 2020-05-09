import os

current_dir = os.path.dirname(__file__)


def get(icon_name):
    return os.path.join(current_dir, icon_name)
