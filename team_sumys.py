import random
import time
import os


# ----------------------------------로고-------------------------------
def Logo():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@&&&&&@@@@#B&@@@@@@@@@@@@@@@&B#@@@@@@@@@@GYYJJJJP&@@@@B5YJJJJYP&@#5YYJJJJJJY#@@@@@@@@@@@@@@@@@@@@@@&B#@@@@@@@@@@@@@@@@&B#@@@@@&###########&@@@@@")
    print("@@@@@G7JJJJ7P@@B!7J@@@&5Y55555Y5#&?77#@@@@@@@&?7GG55GG7?#@B7?PGP5PBGJ!GJ!G#GPPPP?!G@@@@@@@@@@#PPPPPPP5P&@?77B@@@@@BP55PB&@@@J7!B@@@B7?JJJJJJJJ??7G@@@@")
    print("@@@BYJJJJJJJYY#B7YJ@@@#JJYJYJ7Y!#&757#@@@@@@@#!Y@?!!J@G~G#!J@P!YPJ7G@Y7J?@5!Y555P#@@@@@@@@@@@Y7??YYYYJY&&?Y7#@@@B?J?JJ???B@@?Y7B@@@#5YYYYYYYYJ75!B@@@@")
    print("@@@BY55?YJJ555#B7YJ@@@G?JYJJYJ7G@&?5?#@@@@@@@@P7YGGG&B?J&P~G&7J@@#!Y@B7Y?&57YYYYYYJYG@@@@@@@@YJJYPPPPPB@&?Y7B&@&7Y?G@@P?JJ&@JY?B@@@G?JJYYYYY5JJY?&@@@@")
    print("@@@@@@B?YJJ#@@@B?YJ@@@&G5YJJJJB@@&?5?#@@@@@@@@G7J#@&&57Y#&YJJ?G@@G!G@P7Y?#&BBGGGGB#G?J&@@@@@@YJYJYYYYJP@@?YJJ?YB?5?&@@#75?&@J5?B@&J?YYYJJYYYY?YJJ?5&@@")
    print("@@@@&PJYJJJJG&@B?5Y@@@P?YYYP#@@@@&?5?#@@@@@@@P7G&5JYJ5#5?B@&&@@#5?P@G75BJYYY55PPPJJ&B7P@@@@@@YYJ5BGGGPP55Y5?PB#&YJJ5##YJJ5@@J5?B@&BGPPGGP?5JGGGGGG#@@@")
    print("@@&5?JYP&#5YJ?GBJ5Y@@@&GJJY@@@@@@@YYY&@@@@@@&?Y@B75&57#&?Y@@GYYYP#BYJG@@@&######GJY&G7G@@@@@@GJYYYYYYY55PY5J#@@@&PYYJJYYP@@@Y5JB@@@BJJG@#JY5@@@@@@@@@@")
    print("@@@BGB&@@@@#GG#BJ5Y@@@@#?5JPGGGGGGPPP#@@@@@@@5JB&B55YB@B?G&JJB&@&5JJ5#@@&YJ555PPG#&G?P@@@@@@@@&&&&&&@@@@@J5J#@@@@@&####@@@@@Y5J#@@@PJYYGP55PGGGGG&@@@@")
    print("@@@@@@@@@@@@@@@#5YG@@@@&P555555555555B@@@@@@@&GYYPGGBG5JG@#JYBBBGGGP?5@@&5YPGBBBG5Y5#@@@@@@@@@@@@@@@@@@@@PY5&@@@@@@@@@@@@@@@PY5&@@@#5555555555555#@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGGB#@@@@&BGGGGGGGB&@@@@&#BGGGB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def Start():
    Logo()
    time.sleep(1)
    os.system("cls")
    Logo()
    time.sleep(1)
    os.system("cls")
    Logo()
    time.sleep(1)
    os.system("cls")
    print("치칸 825 타이쿤 시작  !!")


# -------------------------------------- 아이템 함수 -------------------------------------------
# 대출 시작 함수 (기태.12.04)
def loan(Netprofit):
    while True:
        print(f"대출금의 한도액은 {round(Netprofit *1.5)} 입니다. 일주일 이자는 100%입니다.")
        loan_request = int(input("얼마를 대출 하시겠습니까?"))
        if loan_request > round(Netprofit*1.5):
            print("대출금의 한도가 넘었습니다.")
            continue
        if loan_request < 0:
            print("장난치지 마쇼")
            continue
        if loan_request <= round(Netprofit*1.5):
            loan_result = loan_request
            print(f"대출금은 {loan_result}입니다. 다음주 갚아야 할 돈은 {loan_result*2}입니다.")
            Net_profit = Netprofit + loan_result
            return Net_profit,loan_result


# 대출 갚는 함수 (기태.12.04)
def payoff(Netprofit, loanresult):
    loan = loanresult * 2
    if loan > Netprofit:
        print("대출금이 계좌에 있는 돈보다 많습니다.")
        print("드럼통에 담겨 바다에 떨어집니다..")
        print("의식이 점점 사라집니다")
        exit()
    if loan == 0:
        print("")
        Net_profit = Netprofit
        return Net_profit
    else:
        print(f"대출금 {loan}을 갚았습니다.")
        Net_profit = Netprofit - loan
        return Net_profit


# 복권 이벤트 (연수.12.04)
def lottery(lott_money):
    lott = 1000000  # 복권 가격은 100만원
    lott_cnt = 10  # 복권 재고
    lott_list = []  # 복권 번호를 입력할 리스트

    if lott_money <= lott:
        pass
    else:
        while True:
            lott_choice = input('복권을 사시겠습니까?(y/n): ')  # 복권 살지 말지 선택
            if lott_choice == 'y':
                while True:
                    # 복권 몇 장 살지 물어보는 입력문
                    if (lott_money // lott) > lott_cnt:  # 복권은 1주일에 10장만 살 수 있음
                        lott_buy = int(input(f'복권을 몇 장 사시겠습니까? (취소: 0)\n'
                                             f'한 장에 백만원, 현재 살 수 있는 복권 수({lott_cnt}장): '))
                    else:  # 복권을 살 수 있는 최대 갯수
                        lott_buy = int(input(f'복권을 몇 장 사시겠습니까? (취소: 0)\n'
                                             f'한 장에 백만원, 현재 살 수 있는 복권 수({lott_money // lott}장): '))
                    if lott_buy == 0:  # 갑자기 마음이 바껴서 복권을 사지 않을 수 있음
                        print('복권을 사지 않기로 했습니다.')
                        return lott_money
                    elif lott_buy < 0:  # 음수 입력해서 뻥튀기 하는 경우 경고문 출력
                        print('장난치지 마쇼;\n')
                        return lott_money
                    elif lott_buy > lott_cnt:  # 재고보다 많이 살 수 없음
                        print('복권 재고가 부족합니다.')
                        continue
                    elif lott_buy > (lott_money // lott):  # 돈이 없는데 복권을 살 수 없음
                        print('돈이 부족합니다.')
                        continue
                    elif lott_buy <= (lott_money // lott):  # 복권 산 갯수만큼 복권 번호 입력
                        lott_money -= (lott_buy * lott)  # 복권 산 만큼 돈에서 지출
                        #prize = random.randint(1, 100)  # 당첨 번호
                        prize = 7  # 당첨 번호

                        i = 0
                        while i < lott_buy:
                            lott_num = (int(input('숫자를 입력해주세요. (1~100): ')))
                            if 0 < lott_num <= 100:
                                lott_list.append(lott_num)
                                i += 1
                            else:
                                print('다시 입력해주세요')
                                continue

                        print(f'\n당첨 번호는 {prize}번 입니다.')
                        if prize in lott_list:  # 당첨되면 상금 3.4억 * n
                            print(f'입력 번호: {lott_list}')
                            lott_money += (340000000 * lott_list.count(prize))
                            print(f'복권에 당첨되셨습니다! {340000000 * lott_list.count(prize)}원을 상금으로 받았습니다!\n'
                                  f'남은 돈: {lott_money}\n')
                            return lott_money
                        else:
                            print(f'입력 번호: {lott_list}')
                            print(f'복권에 당첨되지 못했습니다...\n'
                                  f'남은 돈: {lott_money}\n')
                            return lott_money
                    else:
                        print('다시 입력해주세요')
                        continue
            elif lott_choice == 'n':
                print('복권을 사지 않기로 했습니다.')
                return lott_money
            else:
                print('다시 입력해주세요')
                continue

# -------------------------------------- 이벤트 함수 -------------------------------------------
# 고용노동부 불시검문 이벤트 (연재.12.04)
def unannounced_inspection(worker):
    
    if worker ==0 :
        fine = 0
        return fine
    if worker <= 100:     # 아르바이트생이 100이하일때 발동
        print("고용노동부에서 근로계약 불시검문을 왔습니다.")
        print("아르바이트생들과 면담이 시작됐습니다.")
        b = random.randint(1, 4)      # 불만 랜덤함수
        unhappy_worker = round(worker // b)   # 불만을 가지는 아르바이트생을 랜덤값으로 나눔
        if unhappy_worker == 0 :
            print("불만 있는 아르바이트생이 없습니다.")
            fine = 0
            return fine
        else :
            fine = 0     
            print(f"{unhappy_worker}명의 아르바이트생이 공무원에게 불만을 토로했습니다.")    # 불만을 가진 아르바이트생 프린트
            print("파견 공무원이 해당 아르바이트생들의 고용계약서를 확인하고 있습니다.")
            c = random.randint(1, 3)      # 고용계약서 문제 확인용 랜덤함수
            if c == 1:
                pm_unhappy_worker = round((unhappy_worker * 0.15)) * 5000000  # 과태료 내야 되는 액수 만들어서 변수에 담기
                print(f"{round(unhappy_worker * 0.15)}명의 아르바이트생의 고용계약서에서 문제가 발견됐습니다.")    # 문제 발견 프린트
                fine = pm_unhappy_worker    # 과태료
                if fine == 0 :
                    print("과태료는 없습니다")
                    return fine
                else :    
                    print(f"{pm_unhappy_worker}원의 과태료를 냈습니다.")    # 과태료 프린트
                    return fine  # 과태료를  리턴
            else:
                print("고용계약서에 아무런 문제가 없습니다.")
                return fine   # 과태료를 리턴

    else:
        print("고용노동부에서 근로계약 불시검문을 왔습니다.")
        print("아르바이트생들과 면담이 시작됐습니다.")
        print("우리 가게는 고용관계가 깨끗합니다.")
        fine = 0
        return fine     # 아무 문제 없는 1주 종합 매출 리턴


# 야구 이벤트 (연재.12.02)
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
            a = guest * 4000    # a에 게스트 곱하기 맥주값한 값을 담아줌
            win_ds_daily_sum = daily - a    # win_ds_daily_sum이라는 새로운 변수를 만들어서 데일리에서 a를 빼줌
            print(f"{a}의 손해를 봤습니다.")    # 12.03(기태) 손해 변수 a로 바꿈

            return win_ds_daily_sum
        else:
            print("엘지 트윈스의 승리...")
            print("고생하셨습니다.")
            return daily
    else:
        return daily


# 일수 이벤트 (기태.12.02)
def meet_gang(final_daily) :
    print("조폭이 나타났다 ...! 오늘의 최종매출액의 절반을 가져갔다")
    #최종매출액의 절반을 가져가고 남은돈 revenue
    revenue = final_daily//2
    print(f"남은 돈은 {round(revenue)}입니다.")
    #소수 값이 나오므로 반올림해서 값을 return 해준다.
    return round(revenue)


# 손님 수를 늘려주는 이벤트(기태.12.02)
def local_event(guest):
    # local = 이벤트 리스트
    local=["단체손님", "주변 지역 행사", "연예인 출몰", "게임 콜라보레이션", "맘카페 주간 맛집 리스트 등극", "드라마 간접출현" , "존잘 알바 등장"]
    #event=이벤트 이름
    event=random.choice(local)
    print(f"{event} 이벤트 발생 !")
    #times = 배율 1.05배에서 2배사이로 설정
    times=random.randrange(105,200)
    #le_guest = 최종 손님
    le_guest = guest * (times /100)
    print(f"손님이 {times /100}배 늘어납니다.")
    return round(le_guest)


# 임대료 이벤트 함수(연수.12.01)
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


# 위생점검 이벤트 함수(의용.12.01)
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

    # 12.03(기태) if 조건문 순서 조정
    # 10점이 4번 나오는 경우 완벽한 위생상태 잭팟
    if hygieneScore == 40:
        print("국가에서 인증받은 기관입니다. 손님이 50% 증가합니다.")
        hy_gn_guest = round(gn_guest * 1.5)
        return hy_gn_guest
    # 1점이 4번 나오는 경우 최악의 위생상태 똥망
    elif hygieneScore == 4:
        print("국가에 위생점검 표적 대상이 되었습니다. 손님이 50% 감소합니다. ")
        hy_gn_guest = round(gn_guest * 0.5)
        return hy_gn_guest
    # 20점의기준은? 만점이 40점이라 공정하게 절반 생각했습니다.
    elif hygieneScore >= 20:
        print("위생점검 합격입니다. 손님이 20% 증가합니다.")
        # round는 반올림함수 소수점 값 제거를 위해 사용함.
        hy_gn_guest = round(gn_guest * 1.2)
        return hy_gn_guest
    elif hygieneScore < 20:
        print("위생점검 불합격입니다.손님이 20% 감소합니다.")
        hy_gn_guest = round(gn_guest * 0.8)
        return hy_gn_guest


# 병원비 이벤트 함수(의용.12.01)
def poison(claim_cnt):      # 클레임 건 사람을 매개변수로 받음
    foodPoisoning = [['CT촬영', 300000], ['X-ray', 100000], ['대변검사', 50000], ['피검사', 50000],
                     ['심전도검사', 50000], ['내과초음파', 50000], ['산부인과초음파', 50000],
                     ['영양제', 300000], ['직장내시경', 100000]]

    hospitalBill = 0    # 병원비는 처음에 0원
    patient = claim_cnt * 0.1   # 클레임 건 사람의 10%가 환자
    patient_cnt = 0     # 병원에 진짜 가는 손님을 세는 변수 (병원을 갈 수도, 자가치료 할수도 있음(착하면))

    print(f'환불 요구하신 손님 {claim_cnt}명중 {round(patient)}명이 병원에 가겠다고 하셨습니다.')
    if round(patient) == 0:    # 12.03 (기태) 0명일때 출력
        print(f"다행입니다")
        return hospitalBill
    else :
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


# 기물파손 이벤트 함수(연수.12.02)
def damaged(dm_claim, dm_daily_sum):
    # 기물 리스트
    arti_list = [['의자', 85000], ['식기', 1500], ['전시용 피규어', 60000], ['식탁', 99000], ['깽값']]
    random.shuffle(arti_list)
    # 분조장 사람들 5%
    mad_people = int(dm_claim * 0.05)
    if int(mad_people) == 0:   # 분조장 사람이 없으면 함수 pass
        pass
    else:
        # 난동 시작
        print(f'\n{mad_people}명이 불만을 몸으로 표출합니다.')
        # 리스트를 섞어주고 0번 1번에 해당되는 리스트 요소만 쓸거임
        if ['깽값'] in arti_list[:2]:
            # 집단 폭행 당하는 우리 사장님 ㅜㅜ
            print(f'손님들을 말리다 상해를 입었습니다. 합의금 {(500000 * mad_people)}원을 받았습니다')
            dm_daily_sum += (500000 * mad_people)
        else:
            # 망가진 기물, 보수 금액 출력
            print(f'{arti_list[0][0]}, {arti_list[1][0]}(이)가 망가졌습니다.'
                  f'보수 금액 {(arti_list[0][1]+arti_list[1][1])*mad_people}이 나왔습니다.')
            dm_daily_sum = dm_daily_sum - ((arti_list[0][1]+arti_list[1][1])*mad_people)
        dm_claim = dm_claim - mad_people

    return dm_claim, dm_daily_sum


# -------------------------------------- 메인 함수 -------------------------------------------
# 손님 수 구하는 함수(연재.11.30)
def guest_num(gn_partTime):     # 함수의 이니셜 + 언더바(_)를 함수의 지역변수들을 구분하기 위해 붙여줬습니다.
    # 손님은 1에서 100명까지
    gn_guest = random.randrange(1, 101)
    random_variable = random.randrange(1,4)
    print('=' * 75)
    if random_variable == 1 :
        gn_guest = local_event(gn_guest)    # 12.02 (기태)
        print('-' * 35)
    if random_variable == 2 :
        # 함수리턴 값을 받아서 새로운 변수에 저장
        gn_guest = hygiene(gn_guest) # 12.02(의용)
    if random_variable == 3 :
        gn_guest = gn_guest
    # 알바가 0이 아닐 때, 손님 수에 알바 수 곱해줌
    if gn_partTime != 0:
        # print(f"손님이 {hygiene_guest * gn_partTime}명 왔습니다.")
        print('')
        return gn_guest * gn_partTime
    # 알바가 없을 때, 손님 수 그대로 출력
    else:
        # print(f"손님이 {hygiene_guest}명 왔습니다.")
        print('')
        return gn_guest


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
    hospital = 0
    # 리펀드 함수의 지역변수 claim에 인자값으로 받은 손님 수 * 0.15 해줬음
    claim = rf_guest * 0.15
    # round함수로 클레임이 소수가 나오면 반올림 시킴
    print(f'{rf_guest}명의 손님 중 15%가 불만이 있습니다. {round(claim)}명입니다.')
    random_variable = random.randrange(1, 3)
    # damage함수 넣어줄 곳. 불만 있는 사람중 몇 명이 난동 -> 불만 품은 사람 - 난동 피운 사람
    if random_variable == 1:
        claim, rf_daily_sum = damaged(claim, rf_daily_sum)  # 12.02 (연수)
    else:
        claim = rf_guest * 0.15
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
    print(f'\n{claim_cnt}명이 음식값을 환불 요청하셨습니다.')
    # refund함수의 환불 변수(receive) = 하루 매출 * (클레임 건 사람 * 0.01) * 2
    # receive = int((rf_daily_sum * (claim_cnt * 0.01)) * 2)

    # refund함수의 환불 변수(rf_refund) = 하루 매출 * (클레임 건 사람 / 총 손님 수) * 2
    rf_refund = int((rf_daily_sum * (claim_cnt / rf_guest)) * 2)
    if claim_cnt == 0 :
        print("다행입니다 ㅎㅎ.")
    else :
        print(f'환불 해줘야 할 금액은 {rf_refund}원입니다.')

    random_variable = random.randrange(1, 5)
    # damage함수 넣어줄 곳. 불만 있는 사람중 몇 명이 난동 -> 불만 품은 사람 - 난동 피운 사람
    if random_variable == 1:
        # 병원비 변수 hospital에 함수 실행값 넣어줌
        hospital = poison(claim_cnt)  # 12.02(의용)
        if hospital == 0:   # 12.03 (기태) 0이면 조건문 pass
            pass
        else:
            print(f'요구받은 병원비는 {hospital}원입니다.')

        # addClaim_daily_sum 변수 = (하루매출) - (환불금액) - (병원비)
    addClaim_daily_sum = rf_daily_sum - rf_refund - hospital
    print(f'\n남은 돈은 {addClaim_daily_sum}원입니다.')
    return addClaim_daily_sum


# 알바 고용한 수, 고용하고 남은 돈 계산 함수, week함수 안에서 쓰입니다.(기태.11.30)
def Hire_worker(netprofit):     # netprofit의 변수명으로 정산금 가격을 받아옴
    if netprofit>0:
        # worker = 0    # 알바생 수는 돈을 줘야 생기므로 매번 0으로 초기화 됨
        # 알바생 수는 정산금을 150만으로 나눈 몫 만큼 생기게 됨.
        worker = netprofit // 1500000
        # 알바생에게 선불금을 지급하고 남은 정산금
        net_profit = netprofit - 1500000 * worker
        return [worker, net_profit]
    else :
        worker = 0
        net_profit = netprofit
        return [worker, net_profit]


# 주간 정산 함수(기태.11.30)
def week(Totalmoney): # Totalmoney = parameter(매개변수)
    # 맨처음 정산금은 0원으로 받아옴
    Net_profit = Totalmoney
    loan_money = 0
    if Net_profit == 0:
        pass
    else :
        it_choice = input('대출을 하시려면 1번, 복권을 사시려면 2번을 입력해주세요: ')
        if it_choice == '1':   # 대출 함수 넣을 곳
            Net_profit, loan_money = loan(Net_profit)
        elif it_choice == '2':
            Net_profit = lottery(Net_profit)       # 로또 사고 남은 돈 반환
        else:
            print('대출, 복권 둘 다 하지 않기로 했습니다.')
    # Hire_worker 함수 실행 , 전주차 정산금을 받아서 알바생을 고용함 / 1주차에는 돈이 없으므로 고용 X
    # 알바생 수(worker)와 알바생 고용 후 남은돈(Net_profit)을 돌려받음
    worker, Net_profit = Hire_worker(Net_profit)
    if worker == 0 : 
        print(f"현재 가진 돈은 {Net_profit}입니다.")
    else :
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
        daily = ks_event(guest, daily)  # 12.02 이벤트 추가(연재)
        # 손님 수와 일일 총 매출을 인수로 하는 환불 (클레임) 함수 실행하여 최종매출액을 변수에 저장 # 이거 프린트 출력되는거 좀 신기함 ㅋㅋ
        final_daily = refund(guest, daily)
        random_variable = random.randrange(1, 5)
        if random_variable == 1:
            final_daily = meet_gang(final_daily)  # 12.02 이벤트 추가 (기태)
        week_sum.append(final_daily)     # 최종 금액을 리스트에 저장
        print('')
        # 임대료 함수 돌리고 당일 임대료를 차감한 매출 리스트 반환, 임대료가 증가하면 증가한 임대료 반환
        week_sum, rental = rentalFc(week_sum, rental, i)    # 12.01 (연수)
        time.sleep(0.25)
    print('=' * 75)
    # 환불금을 해결한 후 1일 최종 매출 함수 표시
    print(f'월요일: {week_sum[0]}원, 화요일: {week_sum[1]}원, 수요일: {week_sum[2]}원,'
          f'\n목요일: {week_sum[3]}원, 금요일: {week_sum[4]}원, 토요일: {week_sum[5]}원, 일요일: {week_sum[6]}원')
    print('=' * 75)
    # 일주일 매출 리스트를 합쳐서 알바생을 고용하고 남은 변수 Net_Profit에 합산
    fine = unannounced_inspection(worker)  # 고용노동부 불시검문 함수 담아서 과태료 만듦 (연재.12.4)
    Net_profit += (sum(week_sum) - fine)  # 고용노동부 불시검문 함수에서 과태료를 가져와 위크썸 매출에서 뺀 값 == 정산값 (연재.12.4)

    Net_profit = payoff(Net_profit,loan_money)      # 12.04(기태)
    print(f"계좌에 있는 돈은 {Net_profit}원입니다")    # 12.03(연수) 팀장 오더로 출력문구 수정
    return Net_profit    # Net_profit 이라는 값을 돌려줌


# 엔딩 함수(기태.11.30)
def ending(Net_profit):
    if Net_profit > 500000000:
        print("마지막주 최종 매출이 5억을 넘겨 프랜차이즈 사업을 시작합니다.")    # 12.03(기태) 출력문구 수정
    else :
        print('마지막주 최종 매출이 5억을 넘지 못했습니다. 게임오버')     # 12.04(기태) 출력문구 수정


# 메인 함수(기태.11.30)
def main():
    # 초반 돈은 0원
    Totalmoney = 0

    Start()
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