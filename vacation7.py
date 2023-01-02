import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

form_class = uic.loadUiType('gwangju.ui')[0]

class MainWindow(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pixmap = QPixmap('Bukgumap.jpg')
        self.map_label.setPixmap(pixmap)

        self.comboBox.addItem('-')
        self.comboBox.addItem('중흥동') #1동, 2동, 3동
        self.comboBox.addItem('중앙동')
        self.comboBox.addItem('임동')
        self.comboBox.addItem('신안동')
        self.comboBox.addItem('용봉동')
        self.comboBox.addItem('운암동') #1동, 2동, 3동
        self.comboBox.addItem('동림동')
        self.comboBox.addItem('우산동')
        self.comboBox.addItem('풍향동')
        self.comboBox.addItem('문화동')
        self.comboBox.addItem('문흥동') #1동, 2동
        self.comboBox.addItem('두암동') #1동, 2동, 3동
        self.comboBox.addItem('삼각동')
        self.comboBox.addItem('일곡동')
        self.comboBox.addItem('매곡동')
        self.comboBox.addItem('오치동') #1동, 2동
        self.comboBox.addItem('석곡동')
        self.comboBox.addItem('건국동')
        self.comboBox.addItem('양산동')
        self.comboBox.addItem('신용동')
        self.comboBox.activated[str].connect(lambda: self.selectedComboItem(self.comboBox))
        self.comboBox_2.addItem('동을 먼저 선택해주세요')
        self.pushButton.clicked.connect(self.search_real)

    def selectedComboItem(self, comboBox):

        self.jh_list = ['중흥1동', '중흥2동', '중흥3동'] #중흥동
        self.ua_list = ['운암1동','운암2동','운암3동'] #운암동
        self.mh_list = ['문흥1동','문흥2동'] #문흥동
        self.da_list = ['두암1동','두암2동','두암3동'] #두암동
        self.oc_list = ['오치1동','오치2동'] #오치동

        if comboBox.currentText() == '중흥동':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.jh_list)

        elif comboBox.currentText() == '운암동':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.ua_list)

        elif comboBox.currentText() == '문흥동':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.mh_list)

        elif comboBox.currentText() == '두암동':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.da_list)

        elif comboBox.currentText() == '오치동':
            self.comboBox_2.clear()
            self.comboBox_2.addItems(self.oc_list)

        else:
            self.comboBox_2.clear()

    def search_real(self):

        check = []
        f = open('gwangju_one.csv', 'r', newline="", encoding='cp949')
        n = csv.reader(f)
        for i in n:
            check.append(i)
        print(check)
        f.close()
        x = self.comboBox.currentText()
        y = self.comboBox_2.currentText()
        print(x)
        print(y)
        search_list_1 = []

        for j in range(len(check)):
            if x in check[j]:
                search_list_1.append(check[j])
            elif x not in check[j]:
                if y in check[j]:
                    search_list_1.append(check[j])
                else:
                    pass
        print("1")
        print(search_list_1)
        self.tableWidget.setRowCount(len(search_list_1))
        self.tableWidget.setColumnCount(7)

        for o in range(len(search_list_1)):
            for p in range(7):
                self.tableWidget.setItem(o, p, QTableWidgetItem(search_list_1[o][p]))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()