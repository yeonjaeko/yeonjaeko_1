import sys

import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets

from firstp import firstwindow
from secondtest import secondwindow
from recheck import checkwindow

List_flower = pd.read_csv('LISTFLOWER_orgin.csv')
List_flower = pd.DataFrame(List_flower)

form_main = uic.loadUiType("search_book.ui")[0]     # ui 파일 불러오기

class mainWindow(QWidget, form_main):
    def __init__(self):
        super().__init__()

        self.allDATA()
        self.setupUi(self)
        self.go_first.clicked.connect(self.buttonClicked_first0)  # 버튼 클릭시 연결되는 함수
        self.go_second.clicked.connect(self.buttonClicked_second0)  #

        self.search_button.clicked.connect(self.searching_bookname)
        self.table_book.doubleClicked.connect(self.Table_DoubleClicked)

    def allDATA(self):
        alldata = List_flower.values
        self.data = []
        for i in alldata:
            self.data.append(list(i))

    def searching_bookname(self):
        # self.all_title = list(List_flower)
        self.fined = []
        #   self.all_title = ['0','연번', ' 소장도서관명', ' 자료실명', ' 등록번호', ' 도서명', ' 저자', ' 출판사', ' 출판연도', ' 청구기호', ' 데이터기준일자', '대여일자', '반납일자', '대여가능여부']
        self.all_title = list(List_flower.columns)
        # 도서명=5, 등록번호=4, 저자=6, 도서관명=2, 11=대여일자, 12=반납일자, 13=대여여부
        self.search_title = [' 소장도서관명'," 등록번호", ' 도서명', ' 저자', '대여여부', '반납일자']
        self.search_index = []
        for i in self.search_title:
            self.search_index.append(self.all_title.index(i))

        self.text = self.search_name.text()
        if self.text == "" or None:
            QtWidgets.QMessageBox.warning(self, "검색오류", "키워드를 입력해주세요")
        else:
            # test = "저자"
            self.list = [" "]
            self.fined = List_flower.loc[List_flower[' 도서명'].str.contains(self.text, na=False)]

            temp_index = self.fined.Index
            self.index_list = []
            for i in temp_index:
                self.index_list.append(i)

            for j in range(1, len(self.all_title)):
                self.list.append(list(self.fined.loc[:, self.all_title[j]]))
            self.showlist()

    def showlist(self):
        self.table_book.setColumnCount(len(self.search_title))
        self.table_book.setRowCount(len(self.index_list))

        for row in range(len(self.index_list)):
            for x in range(len(self.search_index)):
                self.table_book.setItem(row, x, QTableWidgetItem(self.data[self.index_list[row]][self.search_index[x]]))

    def buttonClicked_first0(self):     # pushButton 클릭되었을때 text상자에 출력해주는 소스
        widget.setCurrentIndex(1)

    def buttonClicked_second0(self):  # pushButton 클릭되었을때 text상자에 출력해주는 소스
        mainwin = secondwindow()
        r = mainwin.showModal()

    def Table_DoubleClicked(self):
        self.selectrow = self.table_book.currentIndex().row()
        # 도서명=5, 등록번호=4, 저자=6, 도서관명=2, 11=대여일자, 12=반납일자, 13=대여여부

        select_book.label_lib.setText(str(self.data[self.index_list[self.selectrow]][2]))
        select_book.label_bookname.setText(str(self.data[self.index_list[self.selectrow]][5]))
        select_book.label_writer.setText(str(self.data[self.index_list[self.selectrow]][6]))
        select_book.label_valuename.setText(str(self.data[self.index_list[self.selectrow]][4]))
        select_book.label_borrowDate.setText(str(self.data[self.index_list[self.selectrow]][12]))
        select_book.label_returnDate.setText(str(self.data[self.index_list[self.selectrow]][13]))
        select_book.label_borrowcheck.setText(str(self.data[self.index_list[self.selectrow]][11]))
        select_book.button_borrow.clicked.connect(self.borrow_booksclick)
        select_book.button_return.clicked.connect(self.return_bookscheck)
        r = select_book.showModal()
        self.checked()

    def borrow_booksclick(self):
        if self.data[self.index_list[self.selectrow]][11] != "O":
            print("대여불가")
            select_book.close()
            QtWidgets.QMessageBox.warning(self, '알림', "이미 대여된 도서입니다.")
        else:
            checking.lb_bookname.setText(self.data[self.index_list[self.selectrow]][5])
            r = checking.showModal()

    def return_bookscheck(self):
        if select_book.label_borrowcheck.text() == 'X':
            QtWidgets.QMessageBox.warning(self, '알림', "반납 완료")
            self.data[mainwin.index_list[mainwin.selectrow]][11] = "O"
            select_book.close()
        else:
            QtWidgets.QMessageBox.warning(self, '알림', "대여한 도서가 아닙니다")


    def checked(self):
        if checking.borrowsignal == True:
            mainwin.data[mainwin.index_list[mainwin.selectrow]][11] = "X"
            print("책빌림")
            checking.borrowsignal = False

#마지막에 데이터 변경 완료.##################################
    def savefile(self):
        newlist = []
        for n in range(len(self.all_title)):
            temps = []
            for i in range(len(self.data)):
                temps.append(self.data[i][n])
            newlist.append(temps)
        newlist2 = dict(zip(self.all_title, newlist))
        ddd = pd.DataFrame(newlist2)
        ddd.to_csv('texttexttext.csv', index=None)
#########################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QStackedWidget()
    mainwin = mainWindow()
    first = firstwindow()
    select_book = secondwindow()
    checking = checkwindow()
    widget.addWidget(mainwin)
    widget.addWidget(first)
    widget.setFixedSize(700, 800)
    widget.show()

    app.exec()
    # mainwin.savefile()