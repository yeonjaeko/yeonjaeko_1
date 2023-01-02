import random
import math

A = ['qatar', 'ecuador', 'senegal', 'netherland']
B = ['england', 'iran', 'usa', 'wales']
C = ['argentina', 'saudi arabia', 'mexico', 'poland']
D = ['france', 'austraila', 'denmark', 'tunisia']
E = ['spain', 'costarica', 'germany', 'japan']
F = ['belgium', 'canada', 'moroco', 'croatia']
G = ['brazil', 'serbia', 'switzerland', 'cameroon']
H = ['portugal', 'ghana', 'uruguay', 'korea']


a = 0 #카타르
b = 0 #에콰도르
c = 0 #세네갈
d = 0 #네덜란드
e = 0 #잉글랜드
f = 0 #이란
g = 0 #미국
h = 0 #웨일스
i = 0 #아르헨티나
j = 0 #사우디아라비아
k = 0 #멕시코
l = 0 #폴란드
m = 0 #프랑스
n = 0 #호주
o = 0 #덴마크
p = 0 #튀니지
q = 0 #스페인
r = 0 #코스타리카
s = 0 #독일
t = 0 #일본
u = 0 #벨기에
v = 0 #캐나다
w = 0 #모로코
x = 0 #크로아티아
y = 0 #브라질
z = 0 #세르비아
a1 = 0 #스위스
b1 = 0 #카메룬
c1 = 0 #포르투칼
d1 = 0 #가나
e1 = 0 #우루과이
f1 = 0 #코리아


print("=====A조=====")
A[0] = math.floor(random.random()*7)
print(A[0])
A[1] = math.floor(random.random()*6)
print(A[1])

if A[0] > A[1]:
    print("카타르의 승리")
    print("카타르가 승점 3점을 얻습니다.")
    a+=3
elif A[0] < A[1]:
    print("에콰도르의 승리")
    print("에콰도르가 승점 3점을 얻습니다.")
    b+=3
else:
    print("무승부")
    print("두 팀이 사이좋게 각각 1점씩 획득합니다.")
    a+=1
    b+=1


A[0] = math.floor(random.random()*7)
print(A[0])
A[2] = math.floor(random.random()*4)
print(A[2])

if A[0] > A[2]:
    print("카타르의 승리")
    print("카타르가 승점 3점을 얻습니다.")
    a+=3
elif A[0] < A[2]:
    print("세네갈의 승리")
    print("세네갈이 승점 3점을 얻습니다.")
    c+=3
else:
    print("무승부")
    print("두 팀이 사이좋게 각각 1점씩 획득합니다.")
    a+=1
    c+=1


A[0] = math.floor(random.random()*7)
print(A[0])
A[3] = math.floor(random.random()*2)
print(A[3])

if A[0] > A[3]:
    print("카타르의 승리")
    print("카타르가 승점 3점을 얻습니다.")
    a+=3
elif A[0] < A[3]:
    print("네덜란드의 승리")
    print("네덜란드가 승점 3점을 얻습니다.")
    d+=3
else:
    print("무승부")
    print("두 팀이 사이좋게 각각 1점씩 획득합니다.")
    a+=1
    d+=1

A[1] = math.floor(random.random()*6)
print(A[1])
A[2] = math.floor(random.random()*4)
print(A[2])

if A[1] > A[2]:
    print("에콰도르의 승리")
    print("에콰도르가 승점 3점을 얻습니다.")
    b+=3
elif A[1] < A[2]:
    print("세네갈의 승리")
    print("세네갈이 승점 3점을 얻습니다.")
    c+=3
else:
    print("무승부")
    print("두 팀이 사이좋게 각각 1점씩 획득합니다.")
    b+=1
    c+=1


A[1] = math.floor(random.random()*6)
print(A[1])
A[3] = math.floor(random.random()*2)
print(A[3])

if A[1] > A[3]:
    print("에콰도르의 승리")
    print("에콰도르가 승점 3점을 얻습니다.")
    b+=3
elif A[1] < A[3]:
    print("네덜란드의 승리")
    print("네덜란드가 승점 3점을 얻습니다.")
    d+=3
else:
    print("무승부")
    print("두 팀이 사이좋게 각각 1점씩 획득합니다.")
    b+=1
    d+=1


A[2] = math.floor(random.random()*4)
print(A[1])
A[3] = math.floor(random.random()*2)
print(A[3])

if A[2] > A[3]:
    print("세네갈의 승리")
    print("세네갈이 승점 3점을 얻습니다.")
    c+=3
elif A[2] < A[3]:
    print("네덜란드의 승리")
    print("네덜란드가 승점 3점을 얻습니다.")
    d+=3
else:
    print("무승부")
    print("두 팀이 사이좋게 각각 1점씩 획득합니다.")
    c+=1
    d+=1

print("=====A조 결과======")
print("카타르 승점")
print(a)

print("에콰도르 승점")
print(b)

print("세네갈 승점")
print(c)

print("네덜란드 승점")
print(d)

print("=================")


