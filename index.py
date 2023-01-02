import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import uic
import csv
from JCW_searchmain import searchedBook
from Login import Login_Page
form_class = uic.loadUiType('lib.ui')[0]

class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.MoveLogin_Page)
        self.pushButton_2.clicked.connect(self.Movesearching)

    def Movesearching(self):
        QWidget.setCurrentIndex(2)

    def MoveLogin_Page(self):
        QWidget.setCurrentIndex(1)

        #메인에서 로그인 총 정보 (회원정보리스트 싹) 다 들고 있어야함.
        #그래서 내가 보낸 정보 기존 정보에 추가 시켜야함.
        #이건 내가 도서정보를 기존 정보에 추가시켜서 정보가 다시 들어올텐데 이걸 저장하고 있어야한다는 뜻.
        #그래서 이 프로그램이 돌아가는 동안 정보가 계속 유기적으로 사용할 수 있어야 하는데
        #지금은 정보를 왓다갓다 못하고 한쪽으로만 이동 중.

#그 책 등록정보 들어간 데이터 받아와서  user_totaldata를 갱신해줘야돼.







if __name__ == '__main__':
    app = QApplication(sys.argv)
    QWidget = QtWidgets.QStackedWidget()
    mainWindow = WindowClass()
    Login_page = Login_Page()
    Search_Page = searchedBook('이야기꽃도서관')

    QWidget.addWidget(mainWindow)
    QWidget.addWidget(Login_page)
    QWidget.addWidget(Search_Page)
    QWidget.setFixedHeight(800)
    QWidget.setFixedWidth(1000)
    QWidget.show()
    app.exec_()



