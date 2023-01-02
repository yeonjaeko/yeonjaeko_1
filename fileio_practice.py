f = open("join.txt", 'w')
students = ['김철수', '최영', '한석규', '김태희']
for student in students:
    a = student
    f.write(a + "\n")

f.close


f = open("join.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close

f = open("join.txt", 'r')
memo = f.read()
print(memo)
f.close()


