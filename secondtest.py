import sys

import pandas as pd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

# List_flower = pd.read_csv('listplower.csv')
form_secondwindow = uic.loadUiType("dialog.ui")[0]

class secondwindow(QDialog, form_secondwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(self.closeclick)
        pixmap = QPixmap('books.png')
        self.lb_img.setPixmap(pixmap)

        # self.button_borrow.clicked.connect(self.checking)

    # def checking(self):
    #     checkingwindow.lb_bookname.setText(self.label_bookname)

    def closeclick(self):
        # print(self.label_valuename.toPlainText())
        self.close()

    # def borrow_books(self):
    #     print(List_flower.loc[List_flower[' 등록번호'] == self.label_valuename.text()])
        # print(index)

    def showModal(self):
        return super().exec_()

