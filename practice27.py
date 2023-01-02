from PySide2.QtWidgets import *


def check_age():
    print(ageedit.text())
    if int(ageedit.text()) > 20:
        agetext.setVisible(True)

def join():
    print(nameedit.text().__len__())
    if nameedit.text().__len__()>=5:
        nametext.setVisible(True)

app=QApplication()
window=QWidget()

layout=QFormLayout()

nameedit=QLineEdit()
layout.addRow("name",nameedit)

nametext=QLabel("아이디의 길이가 길어요...")
nametext.setVisible(False)
layout.addWidget(nametext)

passedit=QLineEdit()
layout.addRow("password",passedit)


sublayout=QHBoxLayout()
ageedit=QLineEdit()
sublayout.addWidget(ageedit)
btn=QPushButton("나이확인")
btn.clicked.connect(check_age)
sublayout.addWidget(btn)

layout.addRow("Age",sublayout)
agetext=QLabel("경고 : 나이가 너무 많습니다")
agetext.setVisible(False)
layout.addWidget(agetext)

joinbtn=QPushButton("회원가입")
joinbtn.clicked.connect(join)
layout.addWidget(joinbtn)

window.setLayout(layout)
window.show()

app.exec_()