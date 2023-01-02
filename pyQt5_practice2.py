import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Login_practice2.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class SecondPage(QWidget, form_class):
    def __init__(self):
        super().__init__()
        #ui 불러오기, 객체 생성
        self.setupUi(self)
        #stack의 페이지를 첫번째 페이지로 고정한다.
        self.stackedWidget.setCurrentIndex(0)
        #버튼의 클릭이벤트와 함수를 연결해준다.
        self.btn_nextPage.clicked.connect(self.next_stack)
        self.btn_prePage.clicked.connect(self.pre_stack)

    def next_stack(self):
        self.stackedWidget.setCurrentIndex(1)

    def pre_stack(self):
        self.stackedWidget.setCurrentIndex(0)


    def MoveMainPage(self):
        print(type(self.parent()))
        self.parent().setCurrentIndex(0)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    SecondPage = SecondPage()

    #프로그램 화면을 보여주는 코드
    SecondPage.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()