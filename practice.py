a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)


a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

a = "pithon"
print(a[:1] + 'y' + a[2:])


a = "pithon"
print(a[:1] + 'y' + a[2:])

a = "pithon"
print(a[:1] + 'y' + a[2:])






a = "Hobby"
b = list(a)
print(a.lower())
print(f"배열의 길이: {len(a)}")

for c in a:
    print(f"{c}의 위치: {a.index(c)}", end=" / ")
    print(f"{c}의 개수: {a.count(c)}")



a = "Hobby"
b = list(a)
print(a.lower())
print(f"배열의 길이: {len(a)}")

for c in a:
    print(f"{c}의 위치: {a.index(c)}", end=" / " )
    print(f"{c}의 개수: {a.count(c)}")



a = "Hobby"
b = list(a)
print(a.upper())
print(f"배열의 길이: {len(a)}")

for c in a:
    print(f"{c}의 위치: {a.index(c)}", end= " / ")
    print(f"{c}의 개수: {a.count(c)}")



a = "Hobby"
b = list(a)
print(a.upper())
print(f"배열의 길이: {len(a)}")

for c in a:
    print(f"{c}의 위치: {a.index(c)}", end= " / ")
    print(f"{c}의 개수: {a.count(c)}")



a = "HOBBY"
b = list(a)
print(a.lower())
print(f"배열의 길이: {len(a)}")

for c in a:
    print(f"{c}의 위치: {a.index(c)}", end=" / ")
    print(f"{c}의 개수: {a.count(c)}",)



a = "Hobby"
b = list(a)

print(b)
print(f"문자열의 길이: {len(b)}")

for i in b:
    # if str_list.count(i) > 1:

    print(f"{i}의 위치: {b.index(i)}", end=" ")
    print(f"{i}의 갯수: {b.count(i)}")

    #변수는 영어 풀네임을 써라
    #예약어 쓰지 마라. 충돌 일어남.



a = " hi "
print(a.lstrip())



a = ['a' , 'c' , 'b']
a.sort()
print(a)

a = ['a' , 'c' , 'b']
a.sort()
a.reverse()
print(a)





dic = {'name': 'pey', 'phone': 1231241421, 'birth': 1118}
print(dic['name'])

#dic[ch]append(idx)

Instring=input('입력:')
Dic ={ }
idx = 0
for ch in Instring:
   if ch not in dic:
     Dic[ch] = [ ]
     dic [ch].append(idx)
     idx+=1



for key in str_list :               #str_list에서 첫번쨰부터 값을 가져오는데 그게 key에 들어가는거.
    if key not in dic :             #key값이 기존 dic에 없으면 동작
        dic[key]=[i]                #dic[key] 첫번째는 dic[g]겠지 거기 첫번째에 i값 저장 이게 인덱스값 0부터 쭉
        i=i+1                       #다음 인덱스 위치 나타낼 수 있게 증가.
    else :                          #dic에 키값이 존재하면
        dic[key].append(i)          #기존 dic[key] 뒤에 i값 추가시켜.
        i=i+1                       #다음 인덱스 위치 나타낼 수 있게 증가.
print(dic)                          #이건 그냥 dic 전체 출력 한번.
print()
for key in dic :                    #이건 이제 반복문 다 지나고 전체 dic을 통해서 원하는 값을 찾아야 하니까.
    print(key, "count :",len(dic[key]), "index :", dic[key])




