import random
import os


def lottery(lott_money):
    lott = 1000000 #복권 가격은 100만원
    lott_cnt = 10  #복권 재고
    lott_list = [] #복권 번호를 입력할 리스트

    if lott_money <= lott:
        pass

    else:
        while True:
            lott_choice = input('복권을 사시겠습니까?(y.n):')
            if lott_choice == 'y':
                while True:
                    #복권 몇 장 살지 물어보는 입력문
                    if (lott_money // lott) > lott_cnt: #복권은 1주일에 10장만 살 수 있음
                       lott_buy = int(input(f'복권을 몇 장 사시겠습니까? (취소: 0) \n'
                                            f'한 장에 백만원, 현재 살 수 있는 복권 수({lott_cnt}장):'))

                    else: #복권을 살 수 있는 최대 갯수
                        lott_buy = int(input(f'복권을 몇 장 사시겠습니까? (취소: 0 )\n'
                                             f'한 장에 백만원, 현재 살 수 있는 복권 수({lott_money // lott}장):'))


                    if lott_buy == 0: #재고보다 많이 살 수 없음
                        print('복권을 사지 않기로 했습니다.')
                        return lott_money

                    elif lott_buy <0 :
                        print('장난치지 마시기 바랍니다. \n')
                        return lott_money

                    elif lott_buy > lott_cnt: #돈이 없는데 복권을 살 순 없음
                        print('복권 재고가 부족합니다.')
                        continue

                    elif lott_buy > (lott_money // lott):
                        print('돈이 부족합니다.')

                    elif lott_buy <= (lott_money // lott): #복권 산 개수만큼 복권 번호 입력
                        lott_money -= (lott_buy * lott) # 복권 산 만큼 돈에서 지출
                        #prize = random.randint(1, 100) # 당첨 번호
                        prize = 7

                        i = 0
                        while i < lott_buy:
                            lott_num = (int(input('숫자를 입력하시오. (1~100):')))
                            if 0 < lott_num <= 100:
                                lott_list.append(lott_num)
                                i += 1

                            else:
                                print('다시 입력해주세요')
                                continue
