# 21번
letters = 'python'
print(letters[0])
print(letters[2])

# 22번
license_plate = '24가 2210'
print(license_plate[3:])

#23번
string = "홀짝홀짝홀짝"
print(string[0:1])
print(string[2:3])
print(string[4:5])
# 슬라이싱 할때 '시작인덱스:끝인덱스:오프셋'을 지정할 수 있습니다.
# 오프셋은 생략이 가능하며, 입력할 경우 해당 숫자만큼 건너뛰면서 계산한다.
print(string[::2])

#24번
string = "PYTHON"
print(string[::-1])

#25번
phone_number = "010-1111-2222"
print(phone_number[0:2] + phone_number[4:8] + phone_number[9:13])
#이게 26번 답이다. replace를 사용하라는 말이었다.
# 파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다. 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)


#26번
phone_number = "010-1111-2222"
print(phone_number[0:3] + phone_number[4:8] + phone_number[9:13])
#이렇게 하는게 아니었다. 다시 한번 replace를 사용해보라는 말이었다.
phone_number2 = phone_number.replace('-','')
print(phone_number2)

#27번
url = "http://sharebook.kr"
url1 = url.split('.')
print(f"{url1[-1]}")

#28번
#lang = 'python'
#lang[0] = 'p'
#preint[lang]
#문자열이 할당 메서드를 지원하지 않는다.

#29번
string = 'abcdfe2a354a32a'
string1 = string.upper()
print(string1)

#30번
string = 'abcd'
string.replace('b', 'B')
print(string)
#문자열은 변형 할 수 없는 객체

#31번
a = "3"
b = "4"
print(a + b)
34
# +는 덧셈이 아닌 문자열의 연결을 의미함

#32번
print("Hi" * 3)
#Hi가 연속으로 3번 나옴. 문자열을 복사하는 방법

#33번
print("-" * 80)

#34번
t1 = 'python'
t2 = 'java'
print(f"{t1}\t{t2}\t{t1}\t{t2}\t{t1}\t{t2}\t{t1}\t{t2}")
#정답은 t3 = t1 + ' ' + t2 + ' ' print(t3 * 4)

#35번
name = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name,age1))
print("이름: %s 나이: %d" % (name2,age2))

#36번
name = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름:  {name} 나이:  {age1}")
print(f"이름:  {name2} 나이:  {age2}")

#37번

name = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름:  {name} 나이:  {age1}")
print(f"이름:  {name2} 나이:  {age2}")

#38번

s = "5,969,782,550"
s1 = s.replace(","," ")
print(s1)


#39번
s = "2020/03(E) (IFRS연결)"
print(s[:7])

#40번
data = "  삼성전자   "
data1 = data.strip()
print(data1)

#41번
ticker = "btc_krw"
ticker2 = ticker.upper()
print(ticker2)

#42번
ticker3 = "BTC_KRW"
ticker4 = ticker3.lower()
print(ticker4)

#43번
a = 'hello'
b = a.upper()
print(b)

#44번
file_name = "보고서.xlsx"
f2 = file_name.endswith("xlsx")
print(f2)

#45번
file_name1 = "보고서.xlsx"
f3 = file_name.endswith("xlsx")
f4 = file_name.endswith("xls")
print(f3)
print(f4)

#46번
file_name2 = "2020_보고서.xlsx"
f5 = file_name2.startswith("2020")
print(f5)

#47번
a = "hello world"
print(a[:5])
print(a[6:11])
#정답은 print(a.split())

#48번
ticker = "btc_krw"
print(ticker.split('_'))

#49번
date = "2020-05-01"
print(date.split('-'))

#50번
data = "039490       "
data = data.rstrip()
print(data)

#51번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#52번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

#53번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
movie_rank.insert(1, "슈펴맨")
print(movie_rank)

#54번
movie_rank =["닥터 스트레인지","슈퍼맨","스플릿","럭키","배트맨"]
del movie_rank[4]
print(movie_rank)

#55번
movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "배트맨"]
del movie_rank[2:]
print(movie_rank)

#56번
lang1 =["c", "c++", "JAVA"]
lang2 =["python", "Go", "c#"]
print(lang1 + lang2)

#57번
nums = [1,2,3,4,5,6,7]

print(min(nums))
print(max(nums))

#58번
nums = [1, 2, 3, 4, 5]
result = sum(nums)
print(result)
#구글링 함

#59번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
result_1 =len(cook)
print(result_1)
# 그냥 print(len(cook)) 하면 된다

#60번
nums = [1, 2, 3, 4, 5]
result_2= sum(nums)
print(result/len(nums))

#61번
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62번
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

#63번
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#64번
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#65번
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66번
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
for i in interest:
    print(i, end ='')
#답: print(" ".join(interest))

#67번
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#68번
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#69번
string = "삼성전자/LG전자/Naver"
a = string.split('/')
print(a)

#70번
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
data.reverse()
print(data)

#71번
my_variable=()

#72번
movie_rank=('닥터스트레인지', '스플릿', '럭키')

#73번
t1 = (1,)

#74번
#튜플은 원래 값을 변경할 수 없음

#75번
t = 1, 2, 3, 4
#튜플은 괄호 없이도 사용 가능

#76번
t = ('a', 'b', 'c')
#마찬가지로 튜플의 원래 값은 변경할 수 없으므로 다시 새로 써야 됨
t = ('A', 'B', 'C')

#77번
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a = list(interest)
print(a)

#78번
interest = ['삼성전자', 'LG전자', 'SK Hynix']
b = tuple(interest)
print(b)

#79번
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
#apple banana cake

#80번
i = ()
for i in range(2,100,2):
    print(i)

#정답:data = tuple(range(2, 100, 2)) / pirnt(data)


#81번**
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)
#소위 언패킹. 파이써닉하게 사고하는 방법이다. valid_score라는 변수에 별을 찍고 패킹하고 싶지 않은 수를 뺀다.
#여기서는  ,_을 활용한 것으로 보인다. 추후에 좀 더 구글링 하고 찾아봐야 될 듯 하다.

#82번
scores2 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _,*valid_score2 =scores2
print(valid_score2)
#이런 괴상한 모양으로도 된다. 재밌다. 답은 변수 a와 b를 앞에 뒀다.

#83번
scores3 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score3, _  = scores3
print(valid_score3)
#심지어 이런 모양으로도 된다. 역시 이것도 변수 a, b를 쓰는게 더 깔끔할거 같다.

#84번
temp={}

#85번
d = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(d)

#86번
d = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
d["죠스바"] = 1200
d["월드콘"] = 1500
print(d)

#87번
d = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(d['메로나'])

#88번
d = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
d['메로나'] = 1300
print(d)

#89번
d = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del d['메로나']
print(d)

#90번
#당연한 얘기지만딕셔너리에 없는걸 인덱싱하면 아무것도 나오지 않는다.

#91번
inventory = {'메로나':[300, 20],'비비빅':[400, 3],'죠스바':[250, 100] }
print(inventory)

#92번
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][0], "원")
#도저히 모르겠어서 답을 봤다. 이런 식으로 하는구나.. 아마 메로나에 저장된 값 중 0번째 걸 꺼내는 방법으로 보인다.

#93번
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print(inventory["메로나"][1], "개")
#예측이 맞았다. 앞으로 자주 사용할 수 있을거 같다.

#94번
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

inventory['월드콘']= 500, 7
print(inventory)

#95번
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream = list['key']
print(icecream)
#우스꽝스러운 내 식을 보라 와
#정답은
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice)
#새로운 변수에 list(icecream.keys())를 넣어준다. 이것도 정말 유용할 것으로 보인다. 앞으로 다양하게 활용해봐야겠다.

#96번
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice2 = list(icecream.values())
print(ice2)
#95번 활용 케이스

#97번
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice3 = list(icecream.values())
print(ice3)
ice4 = sum(ice3)
print(ice4)

#98번
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

#append가 안 먹혀서 구글링 해보니 update를 쓰면 된다.
#정답
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#99번
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#100번
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)