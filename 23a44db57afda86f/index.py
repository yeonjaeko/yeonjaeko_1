import sys
# import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

# import MySQLdb
# df = pd.read_csv("첨단도서관.csv")
# print(df)
ui,_ = loadUiType('lib.ui')
# form_class = uic.loadUiType('library.ui')[0]
# form_class = uic.loadUiType(form)[0]
class WindowClass(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        # QMainWindow.__init__(self)
        self.setupUi(self)
        # self.pushButton.setEnable(True)


        #
        # self.btn_1.clicked.connect(self.Open_Login_Tab)
        # self.btn_2.clicked.connect(self.Open_Signup_Tab)
        # self.btn_3.clicked.connect(self.Open_Notice_Tab)


     #-----------------------------------------------#
     # 버튼 클릭 후 보여주는 탭 표시하는 함수 #
    # def Open_Login_Tab(self):
    #     self.tabWidget.setCurrentIndex(0)
    #
    # def Open_Signup_Tab(self):
    #     self.tabWidget.setCurrentIndex(1)
    # #
    # def Open_Notice_Tab(self):
    #     self.tabWidget.setCurrentIndex(2)
    #
    # def Open_Suggestion_Tab(self):
    #     self.tabWidget.setCurrentIndex(3)
    # #
    # def Open_Search_Tab(self):
    #     self.tabWidget.setCurrentIndex(4)
    # #
    # def Open_Rental_Tab(self):
    #     self.tabWidget.setCurrentIndex(5)
    #
    # def Open_Rental_Tab(self):
    #     self.tabWidget.setCurrentIndex(6)

    # def Add_New_Book(self):
    #     # 데이터 베이스 연결
    #     self.db = MySQLdb.connect(host='localhost' , user='root' , password = 'toor', db ='library')
    #     self.cur = self.db.cursor() # 데이터 베이스 상 점 커서를 연결한다.

        # book_title = self.lineEdit_2.text()
        # book_code = self.lineEdit_3.text()
        # book_category = self.comboBox_3.CurrentText()
        # book_author = self.comboBox_4.CurrentText()
        # book_publisher = self.comboBox_5.CurrentText()

    # def Add_Category(self):
    #     self.db = MySQLdb.connect(host='localhost' , user='root' , password = 'toor', db ='library')
    #     self.cur = self.db.cursor() # 데이터 베이스 상 점 커서를 연결한다.
    #
    #     category_name = self.lineEdit_19.text()
    #
    #     self.cur.execute('''
    #         INSERT INTO category (category_name) VALUES (%s)
    #     ''') # 점원을 말하는 듯하다.
    #
    #     self.db.commit()
    #     print('done')
    # def Add_Author(self):
    #     pass
    #
    # def Add_Publisher(self):
    #     pass



def main():
    app = QApplication(sys.argv)
    # widget = QtWidgets.QStackedWidget()
    window = WindowClass()

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()