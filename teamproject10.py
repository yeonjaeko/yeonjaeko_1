import random

#12월 2일 고연재 야구 이벤트 최종 수정
def ks_event(guest, daily):  # 코리아 시리즈 7차전 실행 함수
    if 1000 <= guest <= 1300:  # 손님이 1000명에서 1300명 사이일때 조건문 발동

        print("코리아 시리즈 7차전 시작합니다. 어서 들어오세요.")
        print("오늘 기아가 이기면 손님 전원에게 카스 1잔 무료 서비스 나갑니다.")

        a = 0  # 승리 시 카스값을 담기 위한 변수
        kor_series = ['기아타이거즈',  # 코시진출팀
                      '엘지트윈스']
        bb_win = random.randint(1, 3)  # 승패 랜덤함수
        if bb_win == 1:  # 기아 승리 조건문
            print(f"{kor_series[0]}의 승리!")
            print(f"약속한대로 손님 전원에게 카스 서비스 나갑니다!")
            a = guest * 4000 #a에 게스트 곱하기 맥주값한 값을 담아줌
            win_ds_daily_sum = daily - a #win_ds_daily_sum이라는 새로운 변수를 만들어서 데일리에서 a를 빼줌
            print(f"{win_ds_daily_sum}의 손해를 봤습니다.")

            return win_ds_daily_sum
        else:
            print("엘지 트윈스의 승리...")
            print("고생하셨습니다.")
            return daily
    else:
        return daily


# 손님 수 구하는 함수(연재.11.30)
def guest_num(gn_partTime):     # 함수의 이니셜 + 언더바(_)를 함수의 지역변수들을 구분하기 위해 붙여줬습니다.
    # 손님은 1에서 100명까지
    gn_guest = random.randrange(1, 101)

    # 위생점검 함수(의용.12.01)
    def hygiene(gn_guest):
        # 딕셔너리를 이용하여, 위생점수 0점에서 시작
        maintainance = {'개인위생관리': 0, '식재료검수': 0, '조리관리': 0, '시설관리': 0}

        print('-' * 75)
        print("\n보건소 위생점검 공무원이 방문했습니다. 위생점검을 시작합니다.\n")

        # 딕셔너리 key값 만큼 반복한다.
        for key in maintainance:
            # 각 항목별로 점수는 1점에서 10점 랜덤으로 매겨짐
            a = random.randint(1, 10)
            # 랜덤으로 나온 값을 value값에 넣어줌
            maintainance[key] = a

        # 위생점검 끝난 후 value 값 표시
        print(maintainance)
        # 위생점수의 합을 새로운 변수에 넣어줌
        hygieneScore = sum(maintainance.values())
        print(f"위생점수는 {hygieneScore}점 입니다.")

        # 20점의기준은? 만점이 40점이라 공정하게 절반 생각했습니다.
        if hygieneScore >= 20:
            print("위생점검 합격입니다. 손님이 20% 증가합니다.")
            # round는 반올림함수 소수점 값 제거를 위해 사용함.
            hy_gn_guest = round(gn_guest * 1.2)
            return hy_gn_guest
        elif hygieneScore < 20:
            print("위생점검 불합격입니다.손님이 20% 감소합니다.")
            hy_gn_guest = round(gn_guest * 0.8)
            return hy_gn_guest
        # 10점이 4번 나오는 경우 완벽한 위생상태 잭팟
        elif hygieneScore == 40:
            print("국가에서 인증받은 기관입니다. 손님이 50% 증가합니다.")
            hy_gn_guest = round(gn_guest * 1.5)
            return hy_gn_guest
        # 1점이 4번 나오는 경우 최악의 위생상태 똥망
        elif hygieneScore == 4:
            print("국가에 위생점검 표적 대상이 되었습니다. 손님이 50% 감소합니다. ")
            hy_gn_guest = round(gn_guest * 0.5)
            return hy_gn_guest

    # 함수리턴 값을 받아서 새로운 변수에 저장
    hygiene_guest = hygiene(gn_guest)

    # 알바가 0이 아닐 때, 손님 수에 알바 수 곱해줌
    if gn_partTime != 0:
        # print(f"손님이 {hygiene_guest * gn_partTime}명 왔습니다.")
        print('')
        return hygiene_guest * gn_partTime
    # 알바가 없을 때, 손님 수 그대로 출력
    else:
        # print(f"손님이 {hygiene_guest}명 왔습니다.")
        print('')
        return hygiene_guest


# 일일 매출 함수(연수.11.30)
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


# 클레임 함수(의용.11.30), 손님수와 하루 매출값을 인자로 받음
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

    # 병원비 함수(의용.12.01)
    def poison(claim_cnt):      # 클레임 건 사람을 매개변수로 받음
        foodPoisoning = [['CT촬영', 300000], ['X-ray', 100000], ['대변검사', 50000], ['피검사', 50000],
                         ['심전도검사', 50000], ['내과초음파', 50000], ['산부인과초음파', 50000],
                         ['영양제', 300000], ['직장내시경', 100000]]

        hospitalBill = 0    # 병원비는 처음에 0원
        patient = claim_cnt * 0.1   # 클레임 건 사람의 10%가 환자
        patient_cnt = 0     # 병원에 진짜 가는 손님을 세는 변수 (병원을 갈 수도, 자가치료 할수도 있음(착하면))

        print(f'클레임을 건 사람 {claim_cnt}명중 {round(patient)}명이 병원에 가겠다고 난동을 피우고 있습니다.')

        for i in range(round(patient)):
            a = random.randrange(2)     # 식중독에 걸릴수도, 안걸릴수도 있는 50대 50의 확률로 다시 반복한다.
            # a가 0이 나오면 병원에 입원 함.
            if a == 0:
                patient_cnt += 1
            else:
                continue
        print(f'병원을 가겠다고 병원비를 요구한 사람은 총 {patient_cnt}명 입니다.')

        for h in range(patient_cnt):    # 병원을 가겠다고 한 사람만큼 반복문 돌림
            # 병원비에 들어갈 항목 선택
            num_foodPoisoning = random.randint(1, 10)
            # 병원에 가겠다고 한 사람이 병원 진료받은 내역(영수증)
            ds_patient_sum = 0

            # 병원 진료받은 내역 만큼 반복문 돌림.
            for num in range(num_foodPoisoning):
                # 0번 진료부터 8번 진료까지 8가지 진료 인덱스 번호를 하나 고르게 합니다.
                choose_foodPoisoning = random.randrange(9)
                # j에 0부터 8까지 숫자 들어감
                for j in range(9):
                    if choose_foodPoisoning == j:       # 손님이 고른 병원진료 항목 인데스번호와 j가 같으면 실행
                        ds_patient_sum += foodPoisoning[j][1]

            hospitalBill += ds_patient_sum

        # print(f'병원비는 총 {hospitalBill}이 나왔습니다. ')
        return hospitalBill

    # refund함수의 환불 변수(receive) = 하루 매출 * (클레임 건 사람 * 0.01) * 2
    # receive = int((rf_daily_sum * (claim_cnt * 0.01)) * 2)

    # refund함수의 환불 변수(rf_refund) = 하루 매출 * (클레임 건 사람 / 총 손님 수) * 2
    rf_refund = int((rf_daily_sum * (claim_cnt / rf_guest)) * 2)
    print(f'환불 해줘야 할 금액은 {rf_refund}원입니다.\n')

    # 병원비 변수 hospital에 함수 실행값 넣어줌
    hospital = poison(claim_cnt)
    print(f'요구받은 병원비는 {hospital}원입니다.')

    # addClaim_daily_sum 변수 = (하루매출) - (환불금액)
    addClaim_daily_sum = rf_daily_sum - rf_refund - hospital
    print(f'\n남은 돈은 {addClaim_daily_sum}원입니다.')
    return addClaim_daily_sum


# 알바 고용한 수, 고용하고 남은 돈 계산 함수, week함수 안에서 쓰입니다.(기태.11.30)
def Hire_worker(netprofit):     # netprofit의 변수명으로 정산금 가격을 받아옴
    # worker = 0    # 알바생 수는 돈을 줘야 생기므로 매번 0으로 초기화 됨
    # 알바생 수는 정산금을 150만으로 나눈 몫 만큼 생기게 됨.
    worker = netprofit // 1500000
    # 알바생에게 선불금을 지급하고 남은 정산금
    net_profit = netprofit - 1500000 * worker
    return [worker, net_profit]


# 주간 정산 함수(기태.11.30)
def week(Totalmoney): # Totalmoney = parameter(매개변수)
    # 맨처음 정산금은 0원으로 받아옴
    Net_profit = Totalmoney

    # Hire_worker 함수 실행 , 전주차 정산금을 받아서 알바생을 고용함 / 1주차에는 돈이 없으므로 고용 X
    # 알바생 수(worker)와 알바생 고용 후 남은돈(Net_profit)을 돌려받음
    worker, Net_profit = Hire_worker(Net_profit)
    print(f"다음 주 아르바이트생 수: {worker}, 남은 정산금: {Net_profit}") # 알바생 수와 남은 정산금 출력

    week_sum = [] # 주간 정산금을 위해 리스트 만들어줌
    # 임대료 (처음엔 50만원)
    rental = 500000
    # 일주일동안 돌아갈 for문
    SomeDay = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    for i in list(SomeDay):
        # 1일차 worker 변수를 받아서 guest라는 값(손님 수)을 돌려주는 함수 실행
        guest = guest_num(worker)
        # guest(손님수) 값 출력
        print(f'{i}에 방문한 손님: {guest}명')
        daily = daily_sales(guest)  # daily = 일일 매출 함수 돌려서 나오는 값을 담을 변수
        # 일일 매출 출력
        print(f'{i} 매출: {daily}원\n')
        # 손님 수와 일일 총 매출을 인수로 하는 환불 (클레임) 함수 실행하여 최종매출액을 변수에 저장 # 이거 프린트 출력되는거 좀 신기함 ㅋㅋ
        win_daily = ks_event(guest, daily)  # 12월 2일 고연재 야구 이벤트 추가
        final_daily = refund(guest, win_daily)#12월 2일 고연재 야구 이벤트를 추가해서 일일매출 결산에 대입


        week_sum.append(final_daily)     # 최종 금액을 리스트에 저장

        print('')
        # 임대료 함수 돌리고 당일 임대료를 차감한 매출 리스트 반환, 임대료가 증가하면 증가한 임대료 반환
        week_sum, rental = rentalFc(week_sum, rental, i)
    print('=' * 75)

    # 환불금을 해결한 후 1일 최종 매출 함수 표시
    print(f'월요일: {week_sum[0]}원, 화요일: {week_sum[1]}원, 수요일: {week_sum[2]}원,'
          f'\n목요일: {week_sum[3]}원, 금요일: {week_sum[4]}원, 토요일: {week_sum[5]}원, 일요일: {week_sum[6]}원')
    print('=' * 75)
    # 일주일 매출 리스트를 합쳐서 알바생을 고용하고 남은 변수 Net_Profit에 합산
    Net_profit += sum(week_sum)
    print(f"이번주 총 매출은 {Net_profit}원입니다")
    return Net_profit    # Net_profit 이라는 값을 돌려줌


# 임대료 함수(연수.12.01)
def rentalFc(rt_week_sum, rt_rental, s_day):
    if len(rt_week_sum) > 1:
        # 뒤에서 첫번째 인덱스(당일 매출)과 두번째 인덱스(전날 매출)을 비교
        if rt_week_sum[-1] > rt_week_sum[-2]:
            # 당일 매출이 전날 매출보다 증가했으면 임대료 10% 증가
            rt_rental = int((rt_rental * 0.1) + rt_rental)
            rt_week_sum[-1] -= rt_rental
            print(f'{s_day} 임대료로 {rt_rental}원을 지불했습니다.')
            print(f'오늘은 {rt_week_sum[-1]}원 벌었습니다')
        # 전날매출보다 덜 벌었으면 임대료 변화없음
        else:
            rt_week_sum[-1] -= rt_rental
            print(f'{s_day} 임대료로 {rt_rental}원을 지불했습니다.')
            print(f'오늘은 {rt_week_sum[-1]}원 벌었습니다')
    # 첫 날은 비교할 값이 없음. 임대료 50만원 차감
    else:
        rt_week_sum[0] -= rt_rental
        print(f'{s_day} 임대료로 {rt_rental}원을 지불했습니다.')
        print(f'오늘은 {rt_week_sum[-1]}원 벌었습니다')
    return rt_week_sum, rt_rental


# 엔딩 함수(기태.11.30)
def ending(정산금):
    if 정산금 > 500000000:
        print("5억을 벌었습니다. 프랜차이즈 사업을 시작합니다.")
    else :
        print('5억을 벌지 못했습니다. 게임오버')


# 메인 함수(기태.11.30)
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