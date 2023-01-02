
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets

form_secondwindow = uic.loadUiType("jcw_bookselect.ui")[0]

class secondwindow(QDialog, form_secondwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(self.closeclick)
        pixmap = QPixmap('books.png')
        self.lb_img.setPixmap(pixmap)

    def checkingg(self):
        if self.label_borrowcheck.text() != "O":
            self.returnsignal = True
            print("1")
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, '알림', "대여한 도서가 아닙니다")
            print("xxxxxxx")
            self.close()

    def closeclick(self):
        self.close()

    def showModal2(self):
        return super().exec_()

