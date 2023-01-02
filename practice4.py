result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

#add 함수는 매개변수 num에서 받은 값을 이전에 계산한 결괏값에 더한 후 돌려주는 함수이다.


result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


#너무 복잡하다. 클래스를 사용해야한다.

def say_myself(name, old, man=true):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
