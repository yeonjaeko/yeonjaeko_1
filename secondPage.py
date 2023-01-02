import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("SecondPage.ui")[0]

class SecondPage(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_nextPage.clicked.connect(self.next_stack)

    def next_stack(self):
        self.stackedWidget.setCurrentIndex(1)


