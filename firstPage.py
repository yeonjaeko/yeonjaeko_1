import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_widget = uic.loadUiType("FirstPage.ui")[0]


class FirstPage(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)