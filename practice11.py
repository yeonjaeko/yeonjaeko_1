import random

parttime=0
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

# 일일 매출 함수(연수)
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
        # 메뉴 몇 개 고를지 선택
        num_menu = random.randint(1, 5)

        # 한 손님이 고른 메뉴의 결산(영수증)
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

def refund(guest, daily_sum):
    claim = guest * 0.15
    print(f'방문한 손님 중 15%가 불만을 풀고 있습니다. 불만을 품은 사람은 {round(claim)}명입니다.')
    cnt = 0
    for k in range(round(claim)):
        a = random.randint(0, 2)
        if a==0:
            cnt += 1
        else:
            continue

    print(f'클레임을 건 사람(환불 요청한 사람)은 총 {cnt}명입니다.')
    receive = int((daily_sum * (cnt*0.01)) * 2)
    print(f'환불 해줘야 할 금액은 {receive}원입니다.')
    finalDaily_sum = daily_sum - receive
    print(f'수고하셨습니다. 최종 매출은 {finalDaily_sum}원입니다.')
    return finalDaily_sum
def Hire_worker (netprofit) : # a 정산금 가격을 받아옴
    worker = 0  # 알바생 수는 돈을 줘야 생기므로 매번 0으로 초기화 됨
    worker = netprofit // 1500000 # 알바생 수는 정산금을 150만으로 나눈 몫 만큼 생기게 됨.
    net_profit = netprofit - 1500000*worker # 알바생에게 선불금을 지급하고 남은 정산금
    return [worker,net_profit]



def ending(정산금):
    if 정산금 > 500000000:
        print("5억을 벌었습니다. 프랜차이즈 사업을 시작합니다.")
    else :
        print('5억을 벌지 못했습니다. 게임오버')
# 일주일 총 매출 리스트 왜 리스트냐면 기태티비가 리스트로 하자고 함
weekend_sum = []
# 일일 매출 함수 돌려서 나오는 값을 담을 변수
daily = 0
# 알바생 수(임의)

def weekend ():
  worker = 0
  for i in range (1,8):
    guest = guest_num(worker)
    print(f'{i}일차 손님 : {guest}')
    daily = daily_sales(guest)
    print(f'{i}일차 매출: {daily}원')
    final_daily = refund(guest, daily)
    weekend_sum.append(final_daily)
    # 환불금을 해결한 후 1일 최종 매출 함수 표시
  print(weekend_sum)
  Net_profit = sum(weekend_sum)
  print(Net_profit)
  Hire_worker(Net_profit)
  worker,Net_profit = Hire_worker(Net_profit)
  print(f"다음 주 아르바이트생 수  : {worker}, 남은 정산금 : {Net_profit}")

weekend()