import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate, Qt
from JCW_bookselect import secondwindow
from JCW_recheck import checkwindow

form_main = uic.loadUiType("jcw_main.ui")[0]     # ui 파일 불러오기

class searchedBook(QWidget, form_main):
    def __init__(self):
        super().__init__()
        self.UserInfo = ["","","",""]
        self.find_UserInfo_book = None
        self.loginsignal = False
        self.libraryName = "이야기꽃도서관"

        self.alldata3 = pd.read_csv('Total_library.csv')
        self.selectrow = 0
        self.allDATA()
        # self.select = secondwindow()
        self.checking = checkwindow()
        self.setupUi(self)
        self.search_button.clicked.connect(self.searching_bookname)
        self.table_book.doubleClicked.connect(self.Table_DoubleClicked)
        self.tableWidget.doubleClicked.connect(self.return_booksEvent_2)

        self.returnmain.clicked.connect(self.Tomain)
        self.returnmain_2.clicked.connect(self.Tomain)
        self.go_returnlist.clicked.connect(self.movereturn)
        self.go_searchlist.clicked.connect(self.movesearch)

        self.all_title = list(self.alldata3.columns)
        self.search_title = [' 소장도서관명', ' 등록번호', ' 도서명', ' 저자', '대여여부', '반납일자']
        self.search_index = []
        for i in self.search_title:
            self.search_index.append(self.all_title.index(i))

        header = self.table_book.horizontalHeader()
        header.resizeSection(0, 100)
        header.resizeSection(1, 100)
        header.resizeSection(2, 200)
        header.resizeSection(3, 100)
        header.resizeSection(4, 90)
        header.resizeSection(5, 100)
        header2 = self.tableWidget.horizontalHeader()
        header2.resizeSection(0, 100)
        header2.resizeSection(1, 100)
        header2.resizeSection(2, 200)
        header2.resizeSection(3, 100)
        header2.resizeSection(4, 90)
        header2.resizeSection(5, 100)

    def movereturn(self):
        self.titlename2.setText(self.libraryName)
        self.show_returnlist()
        self.stack_search.setCurrentIndex(1)
    def movesearch(self):
        # self.titlename.setText(self.libraryName)
        self.tableWidget.clear()
        # self.showlist()
        self.stack_search.setCurrentIndex(0)

    def Tomain(self):
        self.search_name.clear()
        self.table_book.clearContents()
        self.close()

    def allDATA(self):
        alldata = self.alldata3.values
        self.data = []
        for i in alldata:
            self.data.append(list(i))

    def searching_bookname(self):
        if self.search_name.text() == "" or self.search_name.text() == None :
            QtWidgets.QMessageBox.warning(self, "검색오류", "키워드를 입력해주세요")
            return
        else:
            # self.all_title = list(List_flower)
            self.fined = []
            #   self.all_title = ['0','연번', ' 소장도서관명', ' 자료실명', ' 등록번호', ' 도서명', ' 저자', ' 출판사', ' 출판연도', ' 청구기호', ' 데이터기준일자', '대여일자', '반납일자', '대여가능여부']
            self.all_title = list(self.alldata3.columns)

            self.text = self.search_name.text()
            # test = "저자"
            self.list = [" "]
            self.index_list = []
            for i in self.data:
                if i[5] == None :
                    continue
                if str(self.text) in str(i[5]):
                    self.index_list.append(i[0])
            self.showlist()

    def showlist(self):
        if self.index_list == None:
            return
        if len(self.index_list) == 0 :
            QtWidgets.QMessageBox.warning(self, '알림', "도서가 없습니다.")
            return
        self.table_book.clear()
        self.table_book.setColumnCount(len(self.search_title))
        self.table_book.setRowCount(len(self.index_list)+1)
        for row in range(len(self.index_list)):
            for x in range(len(self.search_index)):
                if self.index_list[row] == None:
                    continue
                if self.data[self.index_list[row]][self.search_index[x]] == "" or self.data[self.index_list[row]][self.search_index[x]] == None :
                    self.table_book.setItem(row, x, QTableWidgetItem("-"))
                else:
                    self.table_book.setItem(row, x, QTableWidgetItem(self.data[self.index_list[row]][self.search_index[x]]))

    def show_returnlist(self):
        self.tableWidget.clear()
        if self.UserInfo == None :
            return
        if self.UserInfo[3] == None:
            return
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        df = pd.read_csv('join55.csv')
        count = 0
        tind = -5
        for i in df["ID"]:                  #id순서대로
            count += 1
            if i == self.UserInfo[0]:       #회원 id리스트 랑 유저 정보 0번(아이디) 비교
                tind = count - 1            #tind 유저인포의 아이디가 몇번쨰 데이터인지 확인
        if tind < 0:
            return
        tempinpo = df.iat[tind, 3]                #책 등록번호
        for i in self.data:                         #전체데이터에서
            if str(tempinpo) == str(i[4]):          #유저에 있는 책등록번호랑 전체데이터의 등록번호가 같으면
                self.find_UserInfo_book = i         #유저 책 정보를 받는다.
                break
        if self.find_UserInfo_book == None:
            return
        print('찾았나?')

        count = 0
        for x in self.search_index:
            print(self.search_index)
            print(type(self.find_UserInfo_book[x]))
            count += 1
            if str(self.find_UserInfo_book[x]) == "" or str(self.find_UserInfo_book[x]) == None:
                self.tableWidget.setItem(0, count - 1, QTableWidgetItem("-"))
            else:
                self.tableWidget.setItem(0, count - 1, QTableWidgetItem(self.find_UserInfo_book[x]))
        print("채우기 완료")

    def return_booksEvent_2(self):
        if self.loginsignal == False or self.UserInfo == None:
            QtWidgets.QMessageBox.warning(self, '알림', "반납은 로그인을 해주세요")
            return
        if self.find_UserInfo_book[2] != self.libraryName:
            QtWidgets.QMessageBox.warning(self, '알림', "해당 도서관의 도서가 아닙니다.")
        else:
            QtWidgets.QMessageBox.warning(self, '알림', "반납 완료")
            self.data[self.find_UserInfo_book[0]][11] = "O"
            self.data[self.find_UserInfo_book[0]][12] = "-"
            self.data[self.find_UserInfo_book[0]][13] = "-"
            self.UserInfo[3] = ''
            self.find_UserInfo_book = None

            df = pd.read_csv('join55.csv')
            tind = -5
            count = 0
            for i in df["ID"]:
                count += 1
                if i == self.UserInfo[0]:
                    tind = count - 1
            if tind < 0 :
                return
            df.iat[tind, 3] = ''
            df.to_csv("join55.csv", index=None)
            print("반납완료")

    def Table_DoubleClicked(self):
        self.select = secondwindow()
        self.selectrow = self.table_book.currentIndex().row()
        if self.data[self.index_list[self.selectrow]][2] == None:
            pass
        else:
            self.select.label_lib.setText(str(self.data[self.index_list[self.selectrow]][2]))
        if self.data[self.index_list[self.selectrow]][5] == None:
            pass
        else:
            self.select.label_bookname.setText(str(self.data[self.index_list[self.selectrow]][5]))
        if self.data[self.index_list[self.selectrow]][6] == None:
            pass
        else:
            self.select.label_writer.setText(str(self.data[self.index_list[self.selectrow]][6]))
        if self.data[self.index_list[self.selectrow]][4] == None:
            pass
        else:
            self.select.label_valuename.setText(str(self.data[self.index_list[self.selectrow]][4]))
        if self.data[self.index_list[self.selectrow]][12] == None:
            pass
        else:
            self.select.label_borrowDate.setText(str(self.data[self.index_list[self.selectrow]][12]))
        if self.data[self.index_list[self.selectrow]][13] == None:
            pass
        else:
            self.select.label_returnDate.setText(str(self.data[self.index_list[self.selectrow]][13]))
        if self.data[self.index_list[self.selectrow]][11] == None:
            pass
        else:
            self.select.label_borrowcheck.setText(str(self.data[self.index_list[self.selectrow]][11]))

        self.select.button_borrow.clicked.connect(self.borrow_booksEvent)
        self.select.button_return.clicked.connect(self.return_booksEvent)   #열리기 전에 데이터 입력
        self.select.showModal2()#창 열림
                                # 창 닫힌 후
                                #새롭게 정의
        self.checked()  #데이터 변경 확인
        self.showlist()   #리스트 갱신


    def borrow_booksEvent(self):
        if self.loginsignal ==False:
            QtWidgets.QMessageBox.warning(self.select, '알림', "로그인 후 이용해 주세요")
            return
        if self.data[self.index_list[self.selectrow]][11] != "O":
            print("대여불가")
            QtWidgets.QMessageBox.warning(self.select, '알림', "이미 대여된 도서입니다.")
        elif self.data[self.index_list[self.selectrow]][2] != self.libraryName:
            QtWidgets.QMessageBox.warning(self.select, '알림', "해당 도서관의 도서가 아닙니다.")
        elif self.UserInfo[3] == "" or self.UserInfo[3] == None or self.UserInfo[3] == " " :
            self.checking.lb_bookname.setText(self.data[self.index_list[self.selectrow]][5])
            self.checking.showModal3()
        else:
            QtWidgets.QMessageBox.warning(self.select, '알림', "이미 대여한 도서가 있습니다.")


    def return_booksEvent(self):
        if self.UserInfo == None:
            QtWidgets.QMessageBox.warning(self.select, '알림', "로그인 후 이용해주세요")
            return
        if self.data[self.index_list[self.selectrow]][2] != self.libraryName:
            QtWidgets.QMessageBox.warning(self.select, '알림', "해당 도서관의 도서가 아닙니다.")
        elif self.UserInfo[3] != self.data[self.index_list[self.selectrow]][4]:
            QtWidgets.QMessageBox.warning(self.select, '알림', "본인이 대여한 도서가 아닙니다.")
        elif self.data[self.index_list[self.selectrow]][11] == "X" and self.data[self.index_list[self.selectrow]][
            2] == self.libraryName and self.UserInfo[3] == self.data[self.index_list[self.selectrow]][4]:
            QtWidgets.QMessageBox.warning(self.select, '알림', "반납 완료")
            self.data[self.index_list[self.selectrow]][11] = "O"
            self.data[self.index_list[self.selectrow]][12] = "-"
            self.data[self.index_list[self.selectrow]][13] = "-"
            self.UserInfo[3] = ''
            self.find_UserInfo_book = None
            self.tableWidget.clear()
            df = pd.read_csv('join55.csv')
            count = 0
            for i in df["ID"]:
                count += 1
                if i == self.UserInfo[0]:
                    tind = count - 1
            df.iat[tind, 3] = ''
            df.to_csv("join55.csv", index=None)

            print("반납완료")
        else:
            QtWidgets.QMessageBox.warning(self.select, '알림', "대여한 도서가 아닙니다")
            print("xxxxxxx")

    def checked(self):
        if self.checking.borrowsignal == None:
            return
        if self.checking.borrowsignal:
            now = QDate.currentDate()
            to = QDate.currentDate().addDays(7)
            self.data[self.index_list[self.selectrow]][12] = now.toString(Qt.ISODate)
            self.data[self.index_list[self.selectrow]][13] = to.toString(Qt.ISODate)
            self.data[self.index_list[self.selectrow]][11] = "X"
            self.UserInfo[3] = self.data[self.index_list[self.selectrow]][4]
            df = pd.read_csv('join55.csv')
            count = 0
            for i in df["ID"]:
                count += 1
                print(i)
                print(self.UserInfo)
                if str(i) == str(self.UserInfo[0]):
                    tind = count - 1
            df.iat[tind, 3] = self.data[self.index_list[self.selectrow]][4]
            df.to_csv("join55.csv", index=None)
            print("책빌림")
            self.checking.borrowsignal = False