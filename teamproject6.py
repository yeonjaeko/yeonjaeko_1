import random

def guest_num(gn_partTime):
    gn_guest = random.randrange(1, 101)

    if gn_partTime != 0:
        print(f"손님이 {gn_guest * gn_partTime}명 왔습니다.")
        return gn_guest * gn_partTime
    else:
        print(f"손님이 {gn_guest}명 왔습니다.")
        return gn_guest


def daily_sales(ds_guest):
    menu = [['후라이드 치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000], ['후라이드 순살', 17000],
            ['양념치킨 순살', 18000], ['간장치킨 순살', 18000], ['마른오징어', 8000], ['과일안주', 15000],
            ['포테이프 후라이', 5000 ], ['쥐포', 7000], ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000],
            ['오비라거', 4500], ['클라우드', 4500], ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000],
            ['오뎅탕', 7000], ['떡볶이', 7000]
            ]

    ds_daily_sum = 0

    for i in range(ds_guest):
        num_menu = random.randint(1, 5)
        ds_guest_sum = 0

        for num in range(num_menu):
            choose_menu = random.randrange(20)

            for j in range(20):
                if choose_menu == j:
                    ds_guest_sum += menu[j][1]

            ds_daily_sum += ds_guest_sum

        return ds_daily_sum

def refund(rf_guest, rf_daily_sum):

    claim = rf_guest * 0.15

    print(f'{rf_guest}명의 손님 중 15%가 불만을 품고 있습니다. 불만을 품은 사람은 {round(claim)}명입니다.')

    claim_cnt = 0
    for k in range(round(claim)):
        a = random.randrange(2)
        if a == 0:
            claim_cnt += 1
        else:
            continue

    rf_refund = int((rf_daily_sum * (claim_cnt / rf_guest)) * 2)
    print(f'{claim_cnt}명의 손님이 클레임을 거셨습니다.')
    print(f'환불 해줘야 할 금액은 {rf_refund}원입니다.')

    addClaim_daily_sum = rf_daily_sum = rf_refund
    print(f'수고하셨습니다. 최종 매출은{addClaim_daily_sum}원 입니다.')
    return addClaim_daily_sum


def Hire_worker(netprofit):
    worker = netprofit // 1500000

    net_profit = netprofit - 1500000 * worker
    return [worker, net_profit]

def week (ToTalmoney):
    Net_profit = ToTalmoney
    worker, Net_profit = Hire_worker(Net_profit)
    print(f"다음 주 아르바이트생 수: {worker}, 남은 정산금: {Net_profit}")

    week_sum = []

    SomeDay = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    for i in list(SomeDay):
        guest = guest_num(worker)
        print('=' * 60)

        print(f'{i}에 방문한 손님: {guest}명')
        daily = daily_sales(guest)

        print(f'{i} 매출: {daily}원')
        final_daily = refund(guest, daily)
        week_sum.append(final_daily)
    print('=' * 60)

    print(f'월요일: {week_sum[0]}원, 화요일: {week_sum[1]}원, 수요일: {week_sum[2]}원,'
          f'목요일: {week_sum[3]}원, 금요일: {week_sum[4]}원, 토요일: {week_sum[5]}원, 일요일: {week_sum[6]}원')

    print('=' * 60)

    Net_profit = sum(week_sum)
    print(f'이번 주 총 매출은 {Net_profit}원입니다.')
    return Net_profit

def ending(정산금):
    if 정산금 > 500000000:
        print('5억을 벌었습니다. 프랜차이즈 사업을 시작합니다.')
    else :
        print('5억을 벌지 못 했습니다. 게임오버')




def main():
    Totalmoney = 0

    First = week(Totalmoney)
    Net_profit = First

    Second = week(Net_profit)
    Net_profit = Second

    Third = week(Net_profit)
    Net_profit = Third

    Fourth = week(Net_profit)


    ending(Fourth)

main()










