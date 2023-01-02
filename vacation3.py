import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QDate, Qt

form_class = uic.loadUiType(("vacation_2.ui"))[0]


class searchedBook(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search_inspection)


    def search_inspection(self):

        check = []
        f = open('cheomdan_lib.csv', 'r', newline="", encoding='UTF-8')
        n = csv.reader(f)
        for i in n:
            check.append(i)
        print(check)
        f.close()

        if self.lineEdit() not in check[4]:
            QMessageBox.warning(self, '.', '검색어를 다시 입력해주세요')
            return



        elif self.lineEdit.text() in check[4]:






if __name__ == "__main__":

    app = QApplication(sys.argv)
    searchedBook = searchedBook()
    searchedBook.show()
    app.exec_()

#
#
# def showall(self):
#
#
#
#         check = []
#         f = open('cheomdan_lib.csv', 'r', newline="", encoding='UTF-8')
#         n = csv.reader(f)
#         for i in n:
#             check.append(i)
#         print(check)
#         f.close()
#
#         self.check = check
#         self.tablewidget = QTableWidget(self)
#         self.tableWidget.setRowCount(len(self.check))
#
#         for z in range(len(self.check) - 1):
#             for y in range(len(self.check[z]) - 1):
#                 self.tableWidget.setItem(z, y, QTableWidgetItem(str(self.check[z + 1][y + 1])))
#
# elf.check = check
#             self.tablewidget = QTableWidget(self)
#             self.tableWidget.setRowCount(len(self.check))

#
# for z in range(len(self.check) - 1):
#     for y in range(len(self.check[z]) - 1):
#         self.tableWidget.setItem(z, y, QTableWidgetItem(str(check[z + 1][y + 1])))

#
# self.tableWidget.setItem(0, 1, QTableWidgetItem(str(check[1])))
# self.tableWidget.setItem(0, 2, QTableWidgetItem(str(check[2])))
# self.tableWidget.setItem(0, 3, QTableWidgetItem(str(check[3])))
# self.tableWidget.setItem(0, 4, QTableWidgetItem(str(check[4])))
# self.tableWidget.setItem(0, 5, QTableWidgetItem(str(check[5])))
# self.tableWidget.setItem(0, 6, QTableWidgetItem(str(check[6])))
# self.tableWidget.setItem(0, 7, QTableWidgetItem(str(check[7])))
# self.tableWidget.setItem(0, 8, QTableWidgetItem(str(check[8])))
# self.tableWidget.setItem(0, 9, QTableWidgetItem(str(check[9])))