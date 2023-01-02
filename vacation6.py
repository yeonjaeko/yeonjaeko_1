from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import sys
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


form_class = uic.loadUiType('vacation_graph.ui')[0]


class MainWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showall)
        self.pushButton_2.clicked.connect(self.search_Year)
        self.lineEdit.setMaxLength(20)
        self.pushButton_2.clicked.connect(self.search_Year)
        self.show()

        #
        # j = []
        # v = []
        # f = open('gwangju_terminal.csv', 'r', newline="", encoding='cp949')
        # n = csv.reader(f)
        # for i in n:
        #     j.append(i[0])
        #     v.append(i[3])
        # print(j)
        # print(v)
        # f.close()
        #
        # self.fig = plt.figure()
        # self.paint = FigureCanvas(self.fig)
        # self.PlotWidget.settext(self.paint)
        # ax = self.fig.add_subplot(211)
        #
        #
        # ax.plot(j, v, color='green', marker='o', linestyle='solid')
        #
        #
        # self.paint.draw()






    def showall(self):
        check = []
        f = open('gwangju_terminal.csv', 'r', newline="", encoding='cp949')
        n = csv.reader(f)
        for i in n:
            check.append(i)
        print(check)
        f.close()

        self.check = check
        self.tableWidget.setRowCount(len(self.check))

        for z in range(len(self.check)):
            for y in range(len(self.check[z])):
                self.tableWidget.setItem(z, y, QTableWidgetItem(str(check[z][y])))





    def search_Year(self):
        check = []
        f = open('gwangju_terminal.csv', 'r', newline="", encoding='cp949')
        n = csv.reader(f)
        for i in n:
            check.append(i)
        print(check)
        f.close()
        self.chose_list = []
        self.check = check
        self.tableWidget.setRowCount(len(self.check))

        for x in range(len(self.check)):
            if self.lineEdit.text() in self.check[x][0]:
                self.chose_list.append(self.check[x])

                self.tableWidget.clear()
                self.tableWidget.setItem(0, 0, QTableWidgetItem(str(check[x][0])))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(str(check[x][1])))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(check[x][2])))
                self.tableWidget.setItem(0, 3, QTableWidgetItem(str(check[x][3])))





if __name__ == "__main__":
        # QApplication : 프로그램을 실행시켜주는 클래스
        app = QApplication(sys.argv)

        # WindowClass의 인스턴스 생성
        main = MainWindow()

        # 프로그램 화면을 보여주는 코드
        main.show()

        # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
        app.exec_()