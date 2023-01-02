import random


# 손님 수 구하는 함수(연재)
def guest_num(parttime):

    while True:
        guest = random.randrange(1, 101)
        if parttime != 0:
          print(f"손님이 {guest * parttime}명 왔습니다.")
          return guest * parttime
        else:
          print(f"손님이 {guest}명 왔습니다.")
          return guest



def daily_sales(guest):
    # 메뉴 변수 2중 리스트로 선언
    menu = [['후라이드 치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000], ['후라이드 순살', 17000],
            ['양념치킨 순살', 18000], ['간장치킨 순살', 18000], ['마른오징어', 8000], ['과일안주', 15000],
            ['포테이프 후라이', 5000], ['쥐포', 7000], ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000],
            ['오비라거', 4500], ['클라우드', 4500], ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000],
            ['오뎅탕', 7000], ['떡볶이', 7000]]
    # 하루 매출 변수 선언
    daily_sum = 0

    #손님 수 만큼 for 돌림
    for i in range(guest):
        num_menu = random.randint(1, 5)


        guest_sum = 0

        # 메뉴 고른 갯수만큼 for문 돌림
        for num in range(num_menu):
            # 0번 메뉴부터 19번 메뉴까지 20가지 메뉴 인덱스 번호를 하나 고르게 합니다.
            choose_menu = random.randrange(20)
            # j에 0부터 19까자 숫자 들어감
            for j in range(20):
                # 손님이 고른 메뉴 인덱스 번호와 i가 같으면 실행
                if choose_menu == j:
                    # 영수증에 손님이 고른 메뉴의 가격 합산
                    guest_sum += menu[j][1]
        daily_sum += guest_sum

    # 하루 매출 변수 return
    return daily_sum













# 일주일 총 매출 리스트 왜 리스트냐면 기태티비가 리스트로 하자고 함
weekend_sum = []
# 일일 매출 함수 돌려서 나오는 값을 담을 변수
daily = 0
# 알바생 수(임의)
parttime = 0

daily = daily_sales(guest_num(parttime))
print(f'1일차 매출: {daily}원')
weekend_sum.append(daily)

daily = daily_sales(guest_num(parttime))
print(f'2일차 매출: {daily}원')
weekend_sum.append(daily)

print(f'일주일 매출: {weekend_sum}')
#
#