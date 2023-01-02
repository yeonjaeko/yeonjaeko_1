import random


# 손님 수 구하는 함수(연재)
def guest_num(gn_partTime):     # 함수의 이니셜 + 언더바(_)를 함수의 지역변수들을 구분하기 위해 붙여줬습니다.
    # 손님은 1에서 100명까지
    gn_guest = random.randrange(1, 101)
    # 알바가 0이 아닐 때, 손님 수에 알바 수 곱해줌
    if gn_partTime != 0:
      print(f"손님이 {gn_guest * gn_partTime}명 왔습니다.")
      return gn_guest * gn_partTime
    # 알바가 없을 때, 손님 수 그대로 출력
    else:
      print(f"손님이 {gn_guest}명 왔습니다.")
      return gn_guest


# 일일 매출 함수(연수)
def daily_sales(ds_guest):
    # 메뉴 변수 2중 리스트로 선언
    menu = [['후라이드 치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000], ['후라이드 순살', 17000],
            ['양념치킨 순살', 18000], ['간장치킨 순살', 18000], ['마른오징어', 8000], ['과일안주', 15000],
            ['포테이프 후라이', 5000], ['쥐포', 7000], ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000],
            ['오비라거', 4500], ['클라우드', 4500], ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000],
            ['오뎅탕', 7000], ['떡볶이', 7000]]
    # 하루 매출 변수 선언
    ds_daily_sum = 0

    #손님 수 만큼 for 돌림
    for i in range(ds_guest):
        # 메뉴 몇 개 고를지 선택
        num_menu = random.randint(1, 5)
        # 한 손님이 고른 메뉴의 결산(영수증)
        ds_guest_sum = 0

        # 메뉴 고른 갯수만큼 for문 돌림
        for num in range(num_menu):
            # 0번 메뉴부터 19번 메뉴까지 20가지 메뉴 인덱스 번호를 하나 고르게 합니다.
            choose_menu = random.randrange(20)
            # j에 0부터 19까자 숫자 들어감
            for j in range(20):
                # 손님이 고른 메뉴 인덱스 번호와 i가 같으면 실행
                if choose_menu == j:
                    # 영수증에 손님이 고른 메뉴의 가격 합산
                    ds_guest_sum += menu[j][1]
        # 오늘의 매출
        ds_daily_sum += ds_guest_sum

    # 하루 매출값 return
    return ds_daily_sum


# 클레임 함수(의용), 손님수와 하루 매출값을 인자로 받음
def refund(rf_guest, rf_daily_sum):
    # 리펀드 함수의 지역변수 claim에 인자값으로 받은 손님 수 * 0.15 해줬음
    claim = rf_guest * 0.15
    # round함수로 클레임이 소수가 나오면 반올림 시킴
    print(f'{rf_guest}명의 손님 중 15%가 불만을 풀고 있습니다. 불만을 품은 사람은 {round(claim)}명입니다.')

    # 클레임을 진짜 걸어버린 손님을 세는 변수 (불만이 있어도 그냥 가거나 클레임을 거는 손님들이 있으니까)
    claim_cnt = 0
    # 전체 손님의 15%(소수면 반올림) 수만큼 반복
    for k in range(round(claim)):
        # 방문한 손님의 15%가 불만을 품어도 클레임을 걸 확률은 50대50
        a = random.randrange(2)
        # a가 0이 나오면 클레임을 검
        if a == 0:
            claim_cnt += 1
        # a가 0이 아닌 그 외의 값이 나오면 클레임을 걸지 않음
        else:
            continue
    # print(f'클레임을 건 사람(환불 요청한 사람)은 총 {claim_cnt}명입니다.')

    # refund함수의 환불 변수(receive) = 하루 매출 * (클레임 건 사람 * 0.01) * 2
    # receive = int((rf_daily_sum * (claim_cnt * 0.01)) * 2)

    # refund함수의 환불 변수(rf_refund) = 하루 매출 * (클레임 건 사람 / 총 손님 수) * 2
    rf_refund = int((rf_daily_sum * (claim_cnt / rf_guest)) * 2)
    print(f'{claim_cnt}명의 손님이 클레임을 거셨습니다.')
    print(f'환불 해줘야 할 금액은 {rf_refund}원입니다.')

    # addClaim_daily_sum 변수 = (하루매출) - (환불금액)
    addClaim_daily_sum = rf_daily_sum - rf_refund
    print(f'수고하셨습니다. 최종 매출은 {addClaim_daily_sum}원입니다.')
    return addClaim_daily_sum


# 알바 고용한 수, 고용하고 남은 돈 계산 함수, week함수 안에서 쓰입니다.(기태)
def Hire_worker(netprofit):     # netprofit의 변수명으로 정산금 가격을 받아옴
    # worker = 0    # 알바생 수는 돈을 줘야 생기므로 매번 0으로 초기화 됨
    # 알바생 수는 정산금을 150만으로 나눈 몫 만큼 생기게 됨.
    worker = netprofit // 1500000
    # 알바생에게 선불금을 지급하고 남은 정산금
    net_profit = netprofit - 1500000 * worker
    return [worker, net_profit]


# 주간 정산 함수(기태)
def week(Totalmoney): # Totalmoney = parameter(매개변수)
    # 맨처음 정산금은 0원으로 받아옴
    Net_profit = Totalmoney
    # Hire_worker 함수 실행 , 전주차 정산금을 받아서 알바생을 고용함 / 1주차에는 돈이 없으므로 고용 X
    # 알바생 수(worker)와 알바생 고용 후 남은돈(Net_profit)을 돌려받음
    worker, Net_profit = Hire_worker(Net_profit)
    print(f"다음 주 아르바이트생 수: {worker}, 남은 정산금: {Net_profit}") # 알바생 수와 남은 정산금 출력

    week_sum = [] # 주간 정산금을 위해 리스트 만들어줌

    # 일주일동안 돌아갈 for문
    SomeDay = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    for i in list(SomeDay):
        # 1일차 worker 변수를 받아서 guest라는 값(손님 수)을 돌려주는 함수 실행
        guest = guest_num(worker)
        print('-' * 60)
        # guest(손님수) 값 출력
        print(f'{i}에 방문한 손님: {guest}명')
        daily = daily_sales(guest)  # daily = 일일 매출 함수 돌려서 나오는 값을 담을 변수
        # 일일 매출 출력
        print(f'{i} 매출: {daily}원')
        # 손님 수와 일일 총 매출을 인수로 하는 환불 (클레임) 함수 실행하여 최종매출액을 변수에 저장 # 이거 프린트 출력되는거 좀 신기함 ㅋㅋ
        final_daily = refund(guest, daily)
        week_sum.append(final_daily)     # 최종 금액을 리스트에 저장
    print('=' * 60)

    # 환불금을 해결한 후 1일 최종 매출 함수 표시
    print(f'월요일: {week_sum[0]}원, 화요일: {week_sum[1]}원, 수요일: {week_sum[2]}원,'
          f'\n목요일: {week_sum[3]}원, 금요일: {week_sum[4]}원, 토요일: {week_sum[5]}원, 일요일: {week_sum[6]}원')
    print('=' * 60)
    # 일주일 매출 리스트를 합쳐서 Net_Profit변수에 저장
    Net_profit = sum(week_sum)
    print(f"이번주 총 매출은 {Net_profit}원입니다")
    return Net_profit # Net_profit 이라는 값을 돌려줌


# 엔딩 함수(기태)
def ending(정산금):
    if 정산금 > 500000000:
        print("5억을 벌었습니다. 프랜차이즈 사업을 시작합니다.")
    else :
        print('5억을 벌지 못했습니다. 게임오버')


# 메인 함수(기태)
def main():
    # 초반 돈은 0원
    Totalmoney = 0

    First = week(Totalmoney)  # 1주차
    Net_profit = First

    Second = week(Net_profit)  # 2주차
    Net_profit = Second

    Third = week(Net_profit)  # 3주차
    Net_profit = Third

    Fourth = week(Net_profit)  # 4주차

    ending(Fourth)  # 4주차 남은돈으로 엔딩 확인

# main함수 실행
main()