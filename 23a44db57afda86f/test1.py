import csv

check = []
f = open('join55.csv', 'r', encoding='utf-8')
n = csv.reader(f)
for i in n:
    check.append(i)
f.close()


input_id = 'qwer'
input_pass = '123'
signal = False
for i in check:
    if i[0] == input_id and i[1] == input_pass:
        signal = True

if signal:
    print("로그인 성공")
    print("%s 님 환영합니다."%i[2])
    if i[4] == "" or i[4] == None:
        print("대여중인 도서가 없습니다.")
    else:
        print("대여중인 도서는 %s 입니다."%i[4])
else:
    print("로그인 실패")
    print("아이디와 비밀번호를 확인하세요")

