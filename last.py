import sys

import pandas as pd
from PyQt5.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PySide2.QtCore import QUrl
from pl import *
from Login import Login_Page
from JCW_searchmain import searchedBook

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.libname = ""
        self.loginpage = Login_Page()
        self.searchpage = searchedBook()
        self.setupUi(self)


    def showsub(self):
        self.searchpage.loginsignal = self.loginpage.loginsignal
        self.searchpage.UserInfo = self.loginpage.loginfo
        self.searchpage.libraryName = self.libname
        self.searchpage.titlename.setText(self.libname)
        self.searchpage.show()


    def logout(self):
        if self.loginpage.loginsignal == False:
            self.loginpage.show()
            self.verticalLayout_6.addWidget(self.pushButton_9)
        if self.loginpage.loginsignal == True:
            QMessageBox.warning(self, '.', '로그인이 되어 있는 상태입니다.')

    def logout2(self):
        if self.loginpage.loginsignal == True:
            self.loginpage.loginsignal = False
            QMessageBox.warning(self, '.', '로그아웃 되었습니다.')


    def singa(self):
        self.libname = "신가도서관"

        self.webEngineView = QWebEngineView()

        self.verticalLayout.addWidget(self.webEngineView)

        self.webEngineView.load(QUrl("https://lib.gwangsan.go.kr/SG/contents/libByIntro"))

        self.show()

        self.webEngineView2 = QWebEngineView()

        self.verticalLayout_2.addWidget(self.webEngineView2)

        self.webEngineView2.load(QUrl("https://lib.gwangsan.go.kr/SG/contents/facilitystatus"))

        self.show()

        self.webEngineView3 = QWebEngineView()

        self.verticalLayout_3.addWidget(self.webEngineView3)

        self.webEngineView3.load(QUrl("https://lib.gwangsan.go.kr/SG/librarian/all"))

        self.show()

        self.webEngineView4 = QWebEngineView()

        self.verticalLayout_4.addWidget(self.webEngineView4)

        self.webEngineView4.load(QUrl("https://lib.gwangsan.go.kr/SG/board/3"))

        self.show()

    def chumdan(self):
        self.libname = "첨단도서관"

        self.webEngineView = QWebEngineView()

        self.verticalLayout.addWidget(self.webEngineView)

        self.webEngineView.load(QUrl("https://lib.gwangsan.go.kr/CD/contents/libByIntro"))

        self.show()

        self.webEngineView2 = QWebEngineView()

        self.verticalLayout_2.addWidget(self.webEngineView2)

        self.webEngineView2.load(QUrl("https://lib.gwangsan.go.kr/CD/contents/facilitystatus"))

        self.show()

        self.webEngineView3 = QWebEngineView()

        self.verticalLayout_3.addWidget(self.webEngineView3)

        self.webEngineView3.load(QUrl("https://lib.gwangsan.go.kr/CD/librarian/all"))

        self.show()

        self.webEngineView4 = QWebEngineView()

        self.verticalLayout_4.addWidget(self.webEngineView4)

        self.webEngineView4.load(QUrl("https://lib.gwangsan.go.kr/CD/board/3"))

        self.show()

    def flower(self):
        self.libname = "이야기꽃도서관"

        self.webEngineView = QWebEngineView()

        self.verticalLayout.addWidget(self.webEngineView)

        self.webEngineView.load(QUrl("https://lib.gwangsan.go.kr/IG/contents/libByIntro"))

        self.show()

        self.webEngineView2 = QWebEngineView()

        self.verticalLayout_2.addWidget(self.webEngineView2)

        self.webEngineView2.load(QUrl("https://lib.gwangsan.go.kr/IG/contents/facilitystatus"))

        self.show()

        self.webEngineView3 = QWebEngineView()

        self.verticalLayout_3.addWidget(self.webEngineView3)

        self.webEngineView3.load(QUrl("https://lib.gwangsan.go.kr/IG/librarian/all"))

        self.show()

        self.webEngineView4 = QWebEngineView()

        self.verticalLayout_4.addWidget(self.webEngineView4)

        self.webEngineView4.load(QUrl("https://lib.gwangsan.go.kr/IG/board/3"))

        self.show()

    def jangduk(self):

        self.libname = "장덕도서관"

        self.webEngineView = QWebEngineView()

        self.verticalLayout.addWidget(self.webEngineView)

        self.webEngineView.load(QUrl("https://lib.gwangsan.go.kr/JD/contents/libByIntro"))

        self.show()

        self.webEngineView2 = QWebEngineView()

        self.verticalLayout_2.addWidget(self.webEngineView2)

        self.webEngineView2.load(QUrl("https://lib.gwangsan.go.kr/JD/contents/facilitystatus"))

        self.show()

        self.webEngineView3 = QWebEngineView()

        self.verticalLayout_3.addWidget(self.webEngineView3)

        self.webEngineView3.load(QUrl("https://lib.gwangsan.go.kr/JD/librarian/all"))

        self.show()

        self.webEngineView4 = QWebEngineView()

        self.verticalLayout_4.addWidget(self.webEngineView4)

        self.webEngineView4.load(QUrl("https://lib.gwangsan.go.kr/JD/board/3"))

        self.show()

    def exit(self):
        # newlist = []
        # for n in range(len(self.searchpage.all_title)):  # all_title은 기존 csv 파일 맨위 열제목: 즉 키값
        #     temps = []
        #     for i in range(len(self.searchpage.data)):  # data 는 기존에 리스트형태로 변환해서 쓰던 totla 책 리스트
        #         temps.append(self.searchpage.data[i][n])
        #     newlist.append(temps)
        # newlist2 = dict(zip(self.searchpage.all_title, newlist))  # 키값 밸류값으로 딕셔너리화
        # ddd = pd.DataFrame(newlist2)  # 데이터프레임 시켜서 csv 로 파일 세이브
        # ddd.to_csv('texttexttext.csv', index=None)
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
