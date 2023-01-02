import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QCheckBox, QHeaderView
from PyQt5.Qt import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #윈도우 설정
        self.setGeometry(200, 100, 400, 400)#X, Y, W, H
        self.setWindowTitle('QTableWidget Sample Window')

        #QTableWidget
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(400, 400)
        self.tablewidget.setRowCount(3) #행의 개수
        self.tablewidget.setColumnCount(3) #열의 개수

        #Sorting 가능한지 여부를 판단한다.
        if not self.tablewidget.isSortingEnabled():
            self.tablewidget.setSortingEnabled(True)




        #큐데이블위젯에 데이터 추가하기
        self.insert_data()


        #체크박스 넣기
        self.chbox1 = QCheckBox()
        self.chbox2 = QCheckBox()



        #체크박스에 시그널 연결
        self.chbox1.stateChanged.connect(self.check_state_checkbox1)
        self.chbox2.stateChanged.connect(self.check_state_checkbox2)



        #셋셀위젯함수를 사용한다.
        self.tablewidget.setCellWidget(0, 0, self.chbox1)
        self.tablewidget.setCellWidget(1, 0, self.chbox2)


        #데이터 조회
        rowcount = self.tablewidget.rowCount()
        colcount = self.tablewidget.columnCount()


        #행과 열 자동으로 수정하기
        self.tablewidget.resizeColumnToContents(3)
        self.tablewidget.resizeRowToContents(3)




        #사이즈로 수정하기 / 함수의 첫번째 인수는 열 번호이며, 두 번째가 열 사이즈입니다.
        # header = self.tablewidget.horizontalHeader()
        # header.resizeSection(0, 10)




        self.tablewidget.item(0, 1).setTextAlignment(Qt.AlignVCenter | Qt.AlignRight )
        self.tablewidget.item(1, 1).setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft )




        #테이블 이벤트 지정
        self.tablewidget.cellChanged.connect(self.cellchanged_event)



        #셀의 포커스가 바뀌었을때 발생하는 currentCellChanged 시그널 구현
        self.tablewidget.currentCellChanged.connect(self.currentcellchanged_event)




        #테이블 이벤트 지정
        self.tablewidget.cellClicked.connect(self.cellclicked_event)
        self.tablewidget.cellDoubleClicked.connect(self.celldoubleclicked_event)




        #행과 열을 반복문으로 돌려서 각 행에 내용물이 있는 지 없는 지 판독
        for i in range(0, rowcount):
            for j in range(0, colcount):
                data = self.tablewidget.item(i, j)
                if data is not None:
                    print(data.text())
                else:
                    print('blank')





    #각 박스에 내용물 입력
    def insert_data(self):
        self.tablewidget.setItem(0, 0, QTableWidgetItem("1행 1열"))
        self.tablewidget.setItem(0, 1, QTableWidgetItem("1행 2열"))
        self.tablewidget.setItem(0, 2, QTableWidgetItem("1행 3열"))
        self.tablewidget.setItem(1, 0, QTableWidgetItem("2행 1열"))
        self.tablewidget.setItem(1, 1, QTableWidgetItem("2행 2열"))
        self.tablewidget.setItem(1, 2, QTableWidgetItem("2행 3열"))
        self.tablewidget.setItem(2, 0, QTableWidgetItem("3행 1열"))
        self.tablewidget.setItem(2, 1, QTableWidgetItem("3행 2열"))
        self.tablewidget.setItem(2, 2, QTableWidgetItem("3행 3열"))
        self.tablewidget.setItem




    #checkbox state 변경 함수
    def check_state_checkbox1(self, state):
        print('chbox1:' +str(state))

    def check_state_checkbox2(self, state):
        print('chbox2:' + str(state))




    #셀의 내용이 바뀌었을때 이벤트
    def cellchanged_event(self, row, col):
        data = self.tablewidget.item(row, col)
        print("cellchanged_event 발생: ", data.text())




    #선택한 셀이 바뀌면 발생하는 이벤트
    def currentcellchanged_event(self, row, col, pre_row, pre_col):
        current_data = self.tablewidget.item(row, col) #현재 선택 셀 값
        pre_data = self.tablewidget.item(pre_row, pre_col)
        if pre_data is not None:
            print("이전 선택 셀 값:", pre_data.text())

        else:
            print("이전 선택 셀 값: 없음")


        print("현재 선택 셀 값:", current_data.text())




    #셀 더블클릭 할때 발생하는 이벤트
    def celldoubleclicked_event(self, row, col):
        data = self.tablewidget.item(row, col)
        print("셀 더블클릭 셀 값:", data.text())




    #셀 선택할때 발생하는 이벤트
    def cellclicked_event(self, row, col):
        data = self.tablewidget.item(row, col)
        print("셀 클릭 셀 값:", data.text())




if __name__ == '__main__':
    app =QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
