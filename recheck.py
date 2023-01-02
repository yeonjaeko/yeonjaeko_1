import sys

import pandas as pd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import uic, QtWidgets

# List_flower = pd.read_csv('listplower.csv')
form_checkingwindow = uic.loadUiType("borrow_rechecking.ui")[0]

class checkwindow(QDialog, form_checkingwindow):
    def __init__(self):
        super().__init__()
        self.borrowsignal = False
        self.setupUi(self)
        self.button_ok.clicked.connect(self.buttonclick_ok)
        self.button_cancel.clicked.connect(self.buttonclick_cancel)
    #
    def buttonclick_ok(self):
        self.borrowsignal = True
        QtWidgets.QMessageBox.warning(self, '알림', "도서 대여 완료.")
        self.close()
    def buttonclick_cancel(self):
        self.borrowsignal = False
        self.close()

    def showModal(self):
        return super().exec_()
