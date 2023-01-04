import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import mysql.connector as mc


form_class = uic.loadUiType("town.ui")[0]


class find_live(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(['-', '문화시설', '체육시설', '편의시설', '학교'])
        self.comboBox_2.addItems(['-','문화시설', '체육시설', '편의시설', '학교'])
        self.comboBox_3.addItems(['-','문화시설', '체육시설', '편의시설', '학교'])
        self.comboBox_4.addItems(['-', '문화시설', '체육시설', '편의시설', '학교'])
        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        self.comboBox_2.currentTextChanged.connect(self.combobox_changed2)
        self.comboBox_3.currentTextChanged.connect(self.combobox_changed3)
    def combobox_changed(self, text):
        index = self.comboBox.findText(text)
        self.comboBox_2.removeItem(index)
    def combobox_changed2(self, text):
        index2 = self.comboBox.findText(text)
        index3 = self.comboBox_2.findText(text)
        self.comboBox_3.removeItem(index2)
        self.comboBox_3.removeItem(index3)

    def combobox_changed3(self, text):
        index4 = self.comboBox.findText(text)
        index5 = self.comboBox_2.findText(text)
        index6 = self.comboBox_3.findText(text)
        self.comboBox_4.removeItem(index4)
        self.comboBox_4.removeItem(index5)
        self.comboBox_4.removeItem(index6)





if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    find_live = find_live()

    # 프로그램 화면을 보여주는 코드
    find_live.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()