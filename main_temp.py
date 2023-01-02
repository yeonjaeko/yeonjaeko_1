import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets

from Login import Login_Page


form_class = uic.loadUiType(("main_temp.ui"))[0]

class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_pushButton.clicked.connect(self.MoveLogin_Page)


    def MoveLogin_Page(self):
        QWidget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QWidget = QtWidgets.QStackedWidget()
    mainWindow = WindowClass()
    Login_Page = Login_Page()


    QWidget.addWidget(mainWindow)
    QWidget.addWidget(Login_Page)

    QWidget.show()

    app.exec_()