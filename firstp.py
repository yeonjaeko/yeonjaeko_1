import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

form_firstwindow = uic.loadUiType("first.ui")[0]

class firstwindow(QWidget, form_firstwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.to_main2.clicked.connect(self.mainto2)
        self.to_second2.clicked.connect(self.secondto2)

    def mainto2(self):
        self.parent().setCurrentIndex(0)

    def secondto2(self):
        pass
        # widget.setCurrentIndex(2)
