
# while treeHit <10:
#     treeHit = treeHit+1
#     print(f"나무를 {treeHit}번 찍었습니다.")
#     if treeHit ==10:
#         print("나무 넘어갑니다.")
#
# for treeHit in range(0, 10):
#     treeHit = treeHit + 1
#     print(f"나무를 {treeHit}번 찍었습니다.")
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# for treeHit in range(1, 11, 1):
#      print(f"나무를 {treeHit}번 찍었습니다.")
#      #if treeHit == 10:
# print("나무 넘어갑니다.")

# coffee = 5
# while True:
#     money = int(input("돈을 넣어주세요"))
#     if money==3000:
#         print("커피가 나왔습니다.")
#         coffee = coffee - 1
#         print(f"커피는 {coffee}개 남았습니다.")
#         if coffee == 0:
#             print("커피를 다 팔았습니다.")
#             break
#     elif money>=3100:
#         print("거스름돈이 나옵니다.")
#         print(f"거스름돈은 {money - 3100} 입니다.")
#         coffee = coffee - 1
#         print(f"커피는 {coffee}개 남았습니다.")
#         if coffee == 0:
#             print("커피를 다 팔았습니다.")
#             break
#
#     else:
#         print("돈이 부족합니다.")
#         break

#
# #
money = 10000
coffee = 10000//500
yuja = 10000//1200
cocoa = 10000//300
#
for a in range(coffee+1):
   for b in range(yuja+1):
         for c in range(cocoa+1):
             sum = (coffee*a) + (yuja*b) + (cocoa*c)
           if a == 0 and b == 0 and c == 0:
            pass
            if sum < money:
              print(f"{a}, {b}, {c}" )


#
# for i in range(1, 9):
#     for j in range(1, 3):
#         print(f"{i}*{j} = {i*j}", end = " ")

#
# money = 10000
# change = 0
# order = 0
# price = 0
# yujacha = 10
# coffee = 10
# cocoa = 10
# beverage =['yujacha', 'coffee', 'cocoa']


#
# print("유   자   차/1200원", "코   코   아/300", "커    피/500")
# print(f"{money}원을 받았습니다.")
#
# for order in range(30):
#     order = int(input("음료수를 골라주세요"))
#     print(f"{order}를 선택하였습니다.")
#
#     if order == 0:
#         print(beverage[0])
#         price+=1200
#         print(f"{beverage[0]}의 가격은 {price}입니다.")
#         print(f"잔돈은{money-price}입니다.")
#
#     elif order == 1:
#         print(beverage[1])
#         price+=500
#         print(f"{beverage[1]}의 가격은 {price}입니다.")
#         print(f"잔돈을{money - price}입니다.")
#
#     elif order == 2:
#         print(beverage[2])
#         price+=300
#         print(f"{beverage[2]}의 가격은 {price}입니다.")
#         print(f"잔돈은{money - price}입니다.")

money = 10000
coffee = 10000//500
yuja = 10000//1200
cocoa = 10000//300
#
for a in range(coffee+1):
   for b in range(yuja+1):
         for c in range(cocoa+1):
             sum = (coffee*a) + (yuja*b) + (cocoa*c)
           if a == 0 and b == 0 and c == 0:
            pass
            if sum < money:
              print(f"{a}, {b}, {c}" )


milk = 300
coffee = 400
cola = 500

for a in range(33):
    if a*milk
