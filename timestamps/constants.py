# -*- coding: utf-8 -*-

import os

# Application variables
APP_VERSION = "1.0.0"
APP_NAME = "Timestamps"
APP_DESCRIPTION = "A quick to use cross-platform time stamp software."
APP_AUTHORS = ["Philip Andersen"]
APP_LICENSE = "GPLv3"
APP_COPYRIGHT = "Copyright © 2018 Philip Andersen"
APP_REPOSITORY = "https://gitlab.com/renegadevi/timestamps"

# Path variables
EXEC_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
PATH_ROOT = os.path.dirname(__file__)
PATH_APP = 'timestamps/'
PATH_RESOURCES = EXEC_PATH + 'resources/'
PATH_ICONS = EXEC_PATH + 'resources/icons/'
PATH_TRANSLATIONS = EXEC_PATH + 'resources/translations/'
PATH_VIEWS = EXEC_PATH + 'views/'
