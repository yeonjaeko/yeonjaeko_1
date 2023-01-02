import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
import csv
form_class = uic.loadUiType("Login.ui")[0]

class Login_Page(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit.setPlaceholderText("영어로 입력")
        self.lineEdit_2.setMaxLength(8)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.join_in.clicked.connect(self.Join)
        self.return1.clicked.connect(self.main)
        self.confirm_3.clicked.connect(self.main)
        self.confirm_3.clicked.connect(self.Join_issue)
        self.inspection_button.clicked.connect(self.Id_inspection)
        self.confirm_1.clicked.connect(self.get_through)
        self.back_to_main.clicked.connect(self.backmain)
        self.loginsignal = False
        self.loginfo = None


    def main(self):
        self.stackedWidget.setCurrentIndex(0)



    def Join(self):
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_3.setPlaceholderText("영어로 입력") #아이디
        self.lineEdit_4.setMaxLength(8) #비밀번호
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_5.setMaxLength(8) #비밀번호 확인
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setPlaceholderText("한글로 입력") #이름
        self.lineEdit_7.setMaxLength(11) #전화번호

    def MoveMainPage(self):
        self.parent().setCurrentIndex(0)


    def Join_issue(self):

        if self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "" or self.lineEdit_5.text() == "" or self.lineEdit_6.text() == "" or self.lineEdit_7.text() == "":
            QMessageBox.warning(self, 'Warning Title', '기재사항을 다 입력해주세요')

        elif self.lineEdit_4.text() != self.lineEdit_5.text():
            QMessageBox.warning(self, 'Warning Title', '비밀번호가 일치하지 않습니다.')

        else:

            f = open('join55.csv', 'a', newline="", encoding='UTF-8')
            wr = csv.writer(f)
            wr.writerow([self.lineEdit_3.text(), self.lineEdit_4.text(),self.lineEdit_6.text()," "])
            f.close()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()

            QMessageBox.information(self, 'message', '회원가입에 성공했습니다.')
            self.stackedWidget.setCurrentIndex(0)


    def Id_inspection(self):
        f = open('join55.csv', 'r', newline="", encoding='UTF-8')
        n = csv.reader(f)
        check = []
        for i in n:
            check.append(i[0])
        if  self.lineEdit_3.text() in check:
            QMessageBox.warning(self, 'Warning Title', '이미 존재하는 아이디입니다.')
        else:
            QMessageBox.information(self, '.', '사용할 수 있는 아이디입니다.')


    def get_through(self):
        check = []
        f = open('join55.csv', 'r', newline="", encoding='UTF-8')
        n = csv.reader(f)
        for i in n:
            check.append(i)
        f.close()

        signal = False
        for i in check:
            if str(i[0]) == self.lineEdit.text() and str(i[1]) == self.lineEdit_2.text():
                signal = True
                self.loginfo = i


        if signal:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            QMessageBox.information(self, '.', '환영합니다.')
            self.loginsignal = True
            self.close()


        else:
            QMessageBox.warning(self, '.', '아이디 또는 비밀번호가 일치하지 않습니다.')


    def backmain(self):
        self.close()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    Login_Page = Login_Page()

    # 프로그램 화면을 보여주는 코드
    Login_Page.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
