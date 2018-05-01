# -*- coding: utf-8 -*-

import os

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUiType

from constants import *

Ui_AboutDialog, AboutDialog = loadUiType(PATH_VIEWS + "AboutDialog.ui")


class AboutDialog(QDialog, Ui_AboutDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        # Update information
        self.ui.label_logo.setPixmap(QPixmap(PATH_ICONS + "64x64.png"))
        self.ui.label_version.setText("Version " + APP_VERSION)
        self.ui.label_copyright.setText(APP_COPYRIGHT)

        # Load html into the about window
        about_html = self.get_folder_file('about.html')
        with open(about_html, 'r', encoding="utf8") as credits:
            self.ui.textBrowser.setHtml(credits.read())

    @staticmethod
    def get_folder_file(file):
        """ Return path of file from within same folder """

        # File path of current folder
        folder_path = os.path.join(os.getcwd(), os.path.dirname(__file__))
        folder_path = os.path.realpath(folder_path)

        # Combine current folder path with file
        file_path = os.path.join(folder_path, file)

        return file_path
