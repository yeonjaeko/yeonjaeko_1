import random

# def ks_event(ks_guest, ks_daily_sum):
#
#
#   if ks_guest in [7, 17, 27, 37, 47, 57, 67, 71, 77]: #특정 숫자의 손님이 올 경우 한국시리즈 7차전 관람 이벤트 시작
#     print("코리아 시리즈 7차전 시작합니다. 어서 들어오세요.")
#     print("오늘 기아가 이기면 손님 전원에게 카스 1잔 무료 서비스 나갑니다.")
#
#     a = 0 #승리 시 카스값을 담기 위한 변수
#     kor_series = ['기아타이거즈', #코시진출팀
#                 '엘지트윈스']
#     bb_win = random.randint(1, 3) #승패 랜덤함수
#   if bb_win == 1: #기아 승리 조건문
#           print(f"{kor_series[0]}의 승리!")
#           print(f"약속한대로 손님 전원에게 카스 서비스 나갑니다!")
#           a = ks_guest * 4000
#           ks_daily_sum -= a
#           return ks_daily_sum
#           print(ks_daily_sum)
#
#   else: #엘지트윈스 승리 조건문
#           print(f"{kor_series[1]}의 승리...")
#           print("고생하셨습니다.")

#
# menu = [['후라이드 치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000], ['후라이드 순살', 17000],
#             ['양념치킨 순살', 18000], ['간장치킨 순살', 18000], ['마른오징어', 8000], ['과일안주', 15000],
#             ['포테이프 후라이', 5000], ['쥐포', 7000], ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000],
#             ['오비라거', 4500], ['클라우드', 4500], ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000],
#             ['오뎅탕', 7000], ['떡볶이', 7000]]




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
        # guest(손님수) 값 출력 # 이곳에 이벤트를 넣어 손님 수를 조정시켜 조정시킨 손님 수를 받는다.
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

