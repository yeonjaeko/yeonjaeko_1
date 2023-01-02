# = "Hobby"
#rint(a.count('H'))
#rint(a.count('b'))
#rint(a.index('H'))
#rint(a.index('b'))
#rint(",".join('Hobby'))




#h    count:1     index:0 /  o  count:1     index:1 이런 식으로 만들어봐라.









a = "Hobby"
b = list(a)
print(list(a))
print(a.lower())
print(f"배열의 길이: {len(a)}")
for c in a:
    print(f"{c}의 위치: {a.index(c)}", end=" / ")
    print(f"{c}의 개수: {a.count(c)}")

a = "Hobby"
b = list(a)
print(list(a))
print(a.lower())
print(f"배열의 길이: {len(a)}")
for c in a:
    print(f"{c}의 위치: {a.index(c)}", end=" / ")
    print(f"{c}의 개수: {a.count(c)}")



