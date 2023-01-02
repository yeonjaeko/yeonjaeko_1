import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets



from firstPage import FirstPage
from secondPage import SecondPage

form_class = uic.loadUiType("MainPage.ui")[0]

class MainPage(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.MoveFirstPage)
        self.pushButton_2.clicked.connect(self.MoveSecondPage)

    def MoveFirstPage(self):
        print("btn_1 Clicked")
        QWidget.setCurrentIndex(1)

    def MoveSecondPage(self):
        print("btn_2 Clicked")
        QWidget.setCurrentIndex(2)



if __name__ == "__main__":
    app =QApplication(sys.argv)
    QWidget = QtWidgets.QStackedWidget()

    MainPage = MainPage()
    firstPage = FirstPage()
    secondPage = SecondPage()

    QWidget.addWidget(MainPage)
    QWidget.addWidget(firstPage)
    QWidget.addWidget(secondPage)

    QWidget.setFixedHeight(875)
    QWidget.setFixedWidth(890)
    QWidget.show()
    app.exec_()
