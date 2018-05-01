#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Timestamps

    Copyright (C) 2018 Philip Andersen <philip.andersen@codeofmagi.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTranslator, QLocale

from views.MainWindow import MainWindow
from constants import *


def main():

    # Initialize application
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(PATH_ICONS + "icon.png"))

    # Localization (will fallback to English)
    translator = QTranslator()
    translator.load(PATH_TRANSLATIONS + str(QLocale.system().name()) + '.qm')
    app.installTranslator(translator)

    # Show main window
    main_window = MainWindow()
    main_window.show()

    # Bind application to system exit
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
