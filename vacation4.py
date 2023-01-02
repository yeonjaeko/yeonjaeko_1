import csv



check = []
f = open('gwangju_one.csv', 'r', newline="", encoding='cp949')
n = csv.reader(f)
for i in n:
    check.append(i)
print(check)
f.close()