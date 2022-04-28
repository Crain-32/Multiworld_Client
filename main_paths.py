import os
import platform

import appdirs

try:
    from sys import _MEIPASS

    ROOT_PATH = _MEIPASS
    IS_RUNNING_FROM_SOURCE = False
    if platform.system() == "Darwin":
        userdata_path = appdirs.user_data_dir("Multiworld_Client", "Multiworld_Client")
        if not os.path.isdir(userdata_path):
            os.mkdir(userdata_path)
        CONFIG_PATH = os.path.join(userdata_path, "config.ini")
    else:
        CONFIG_PATH = os.path.join(".", "config.ini")
except ImportError:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    IS_RUNNING_FROM_SOURCE = True
    CONFIG_PATH = os.path.join(ROOT_PATH, "config.ini")

DATA_PATH = os.path.join(ROOT_PATH, "Data")
