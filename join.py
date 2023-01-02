import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("login.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.window_login.clicked.connect(self.login)
        self.window_join.clicked.connect(self.join)
        self.window_search.clicked.connect(self.search)
        self.window_rental.clicked.connect(self.rental)
        self.return1.clicked.connect(self.main)
        self.return2.clicked.connect(self.main)
        self.return3.clicked.connect(self.main)
        self.return4.clicked.connect(self.main)

    def main(self):
        self.stackedWidget.setCurrentIndex(0)

    def login(self):
        self.stackedWidget.setCurrentIndex(1)
        self.pwLineEdit.setEchoMode(QLineEdit.Password)
        self.pwLineEdit.setMaxLength(8)
        self.pwLineEdit.setPlaceholderText("8자 이내 입력")
        self.idLineEdit.setPlaceholderText("영어로 입력")

    def join(self):
        self.stackedWidget.setCurrentIndex(2)
        self.idLineEdit_2.setPlaceholderText("영어로 입력")
        self.pwLineEdit_3.setMaxLength(8)
        self.pwLineEdit_3.setPlaceholderText("8자 이내 입력")
        self.pwLineEdit_3.setEchoMode(QLineEdit.Password)
        self.pwLineEdit_2.setMaxLength(8)
        self.pwLineEdit_2.setPlaceholderText("8자 이내 입력")
        self.pwLineEdit_3.setEchoMode(QLineEdit.Password)

    def search(self):
        self.stackedWidget.setCurrentIndex(3)

    def rental(self):
        self.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()