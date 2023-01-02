import random
import time
import keyboard


# 키보드 함수(import keyboard 필요) // 박규환 221210 1716
def key_board_move():
    # 정상적인 입력값이 나올 때까지 반복
    while True:
        # 반환 조건
        if keyboard.is_pressed('left'):
            # 입력값이 정상일 경우 정상적으로 반환
            return 'a'
        elif keyboard.is_pressed('right'):
            return 'd'
        elif keyboard.is_pressed('up'):
            return 'w'
        elif keyboard.is_pressed('down'):
            return 's'
        # 입력값이 해당 없을 경우
        else:
            # 패스 후 반복
            pass


# 전투중 키보드 함수 // 박규환 221211 1306
def key_board_battle():
    while True:
        if keyboard.is_pressed('1'):
            return '1'
        elif keyboard.is_pressed('2'):
            return '2'
        elif keyboard.is_pressed('3'):
            return '3'
        else:
            pass


# 엘릭서(무적 아이템) // 박규환 221211 0328
def elixir(elixir_char, potion):
    # 엘릭서가 없을 경우 엘릭서없음 메세지 출력 및 0 반환
    if potion[1] == 0:
        print("엘릭서가 없습니다.")
        return 0
    # 엘릭서가 있을 경우 1개 차감 및 10(턴) 반환
    else:
        print(f"{elixir_char[0]}(이)가 무적 상태에 돌입합니다.")
        potion[1] -= 1
        return 10


 # 배열 함수 a,b는 좌표를 나타냄, floor는 층수를 나타내고 4부터 시작함
def arr(a, b, floor, compre):
    # 임의적으로 15*15배열을 만듬 배경으로 검은색 하트를 넣음
    array = [['🖤' for col in range(15)] for row in range(15)]
    # a는 x좌표 행을 나타냄, b는 y좌표 열을 나타냄 ,초코의용이 (0,0)일때 네모서리, 네 모서리 사이, 그외의 8개가 찍히는경우 총 9가지 조건
    if a == 0 and b == 0:
        # 초코의용의 y좌표에 1을 더한값에 하트
        array[a][b + 1] = '❤'
        # 초코의용의 x좌표에 1을 더한값에 하트
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if a == 0 and 0 < b < 14:
        array[a][b - 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if 0 < a < 14 and b == 0:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
    if a == 14 and b == 0:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
    if a == 14 and 0 < b < 14:
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
        array[a][b + 1] = '❤'
        array[a][b - 1] = '❤'
        array[a - 1][b - 1] = '❤'
    if a == 14 and b == 14:
        array[a][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a - 1][b - 1] = '❤'
    if a == 0 and b == 14:
        array[a][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b - 1] = '❤'
    if 0 < a < 14 and b == 14:
        array[a + 1][b] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a][b - 1] = '❤'
        array[a - 1][b - 1] = '❤'
    if 0 < a < 14 and 0 < b < 14:
        array[a][b - 1] = '❤'
        array[a][b + 1] = '❤'
        array[a + 1][b - 1] = '❤'
        array[a + 1][b] = '❤'
        array[a + 1][b + 1] = '❤'
        array[a - 1][b - 1] = '❤'
        array[a - 1][b] = '❤'
        array[a - 1][b + 1] = '❤'
    # 1~9까지 k값
    for k in range(1, 10):
        # 6~10까지 h값, 총 9*5 몬스터 45마리생성, 팀원과 논의로 맵크기 의 20%를 몬스터 수를 정하기로 하였음. 45마리
        for h in range(6, 11):
            # compare는 1부터 14까지 리스트를 셔플한 값임, 실행을 누를 때마다 재배치 되도록 사용
            if a - 1 <= compre[k] <= a + 1 and b - 1 <= compre[h] <= b + 1:
                # compare[k]는 x좌표, x좌표에서 1을뺀값 부터 1을 더한값까지 ,compare[h]는 y좌표, y좌표 1을 뺀값 부터 1을 더한값까지 몬스터가 표시되도록 하였음
                array[compre[k]][compre[h]] = '🐉'
    # 초코의용 생성, 초기값은 (0,0)
    array[a][b] = '🐱‍'
    # 4,5일떄만 포탈을 생성하고 6일떄는 생성안하도록
    if floor != 6:
        # 포탈생성 앞에 좌표 고정 , 뒤에좌표 floor로 한 이유는 층이 변할 때마다 랜덤으로 포탈위치를 바꾸기 위함.
        array[compre[2]][compre[floor]] = '💠'
        # array에서 생성한 배열을 15*15로 end로 붙이고 개행을 하여 배열완성하는 포문
    for i in array:
        for j in i:
            print(j, end='')
        print()
        # 리턴값으로 array를 받아서 whire_arr에서 사용하기 위함
    return array

# 1층을 통한 와일문, floor_i는 4초기값 층, compre는 1부터 14까지 셔플된 리스트-실행시마다 랜덤재배치 위함, 포션을 메인함수에서 가져옴
# uy는 의용이의 상태창
def while_arr(floor_i, compre, potion, uy):
    # 행,x좌표
    a = 0
    # 열, y좌표
    b = 0
    # 이동을 나타내기 위한 변수
    move = 0
    # 의용이가 포탈과 만날 때까지 진행하는 반복문, 1층 반복문
    while True:
        # 방향키를 한번눌렀을 때 50%확률로 포션 획득을 위한 랜덤변수
        get = random.randint(1, 2)
        # 몇층인지 알려주는 출력문
        print(f"=={floor_i - 3}층맵==")
        # 좌변은 arr함수의 리턴값인 array를 불러오고 우변은 arr함수를 호출하기 위함
        array_while = arr(a, b, floor_i, compre)
        # keyboard를 사용하여 input 제거하고 출력문만 나타냄
        print("방향키를 입력해주세요")
        # 방향키를 한번 누를 때마다 1씩 증감하도록함
        move += 1
        print(f"{move}이동")
        # 키보드의 올바른 작동을 위해 0.1초의 시간지연을 줌
        time.sleep(0.1)
        # 1부터 13까지 랜덤값을 가지게함
        move_a = random.randint(1, 13)
        # 6부터 13까지 랜덤값을 가지게 함
        move_b = random.randint(6, 13)
        # 움직임이 3의 배수 일 때 배치가 바뀌게 하였음
        if move % 3 == 0:
            # 배열의 위치가 x좌표가 compre[0], y좌표가 compre[1] 그것을 랜덤값을 가진 move_b,move_a 로 바뀌게 하여 3턴 마다 바뀌게 하였음
            compre[0], compre[1] = compre[move_b], compre[move_a]
            compre[1], compre[7] = compre[move_b], compre[move_a]
            # 키보드 함수에서 right를 누르면 리턴값으로 d를 받기로 하였음
        if key_board_move() == 'd':
            # b가 14인경우는 벽에 닿으므로 제외하기 위한 조건
            if b < 14:
                # 오른쪽을 누르면 b에 1이 더해지므로 그위치에 몬스터가 있으면 출력문이 나오도록함
                if array_while[a][b+1] == '🐉':
                    print("몬스터 출현했습니다")
                    # 몬스터 대결 함수를 가져오면서 매개변수로 uy, potion을 가져옴
                    vs(monster_status(monster_meet()), uy, potion)
                else:
                    print("몬스터가 없습니다")
                    # 움직일떄마다 1을 더하도록함
                b += 1
                # get이란 랜덤변수는 1부터 2, 1이 될때 포션을 획득하도록 함
                if get == 1:
                    # potion[0,0]은 메인함수에서 선언하였음, 앞에 값은 포션, 뒤에 값은 엘릭서임 , 포션수를 1씩 증가하게 함
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                # 벽에 다달랐을때 값고정을 함
                b = 14
        # 왼쪽을 눌렀을때 함수에서 리턴으로 a를 가짐
        elif key_board_move() == 'a':
            #b==0을 제외하기 위함
            if b > 0:
                if array_while[a][b-1] == '🐉':
                    print("몬스터 출현했습니다")
                    vs(monster_status(monster_meet()), uy, potion)
                else:
                    print("몬스터가 없습니다")
                b -= 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                b = 0

        elif key_board_move() == 's':
            if a < 14:
                if array_while[a+1][b] == '🐉':
                    print("몬스터 출현했습니다")
                    vs(monster_status(monster_meet()), uy, potion)
                else:
                    print("몬스터가 없습니다")
                a += 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")

            else:
                a = 14

        elif key_board_move() == 'w':
            if a > 0:
                if array_while[a-1][b] == '🐉':
                    print("몬스터 출현했습니다")
                    vs(monster_status(monster_meet()), uy, potion)
                else:
                    print("몬스터가 없습니다")
                a -= 1
                if get == 1:
                    potion[0] += 1
                    print(f"포션을 획득하셨습니다. 현재 포션수:{potion[0]}개")
            else:
                a = 0
        else:
            pass
        # 만약 초코의용군의 좌표(a,b)가 포탈의 위치하고 같고 floor_i가 6이 아닐때의 조건
        # floor_i는 초기값4, 1층에서는 4 2층에서는 5 3층에선 6이되므로// 1,2층에서만 발동
        if (a, b) == (compre[2], compre[floor_i]) and floor_i != 6:
            print("👏👏👏👏👏👏👏👏👏👏👏👏👏👏")
            # 브레이크를 걸어 whire_arr(1개 층을 나타내는 함수) 을 나가도록 함
            break


# 포션획득(50%확률)  - 김명은
def water_medicine(potion):
    venti = random.randint(0, 1)
    if venti == 1:
        print('🍖🥩포션을 획득하였습니다.🥩🍖')
        # 0.5%의 랜덤확률
        if random.randint(1, 200) == 1:
            # elixir의 갯수
            potion[1] += 1
            print('✨✨엘릭서를 획득하였습니다.✨✨')
        else:
            # potion 갯수 +1개
            potion[0] += 1
    else:
        pass
    # 포션, 엘릭서를 저장
    return potion


# 포션만피로회복 - 김명은
def water_medicine_drink(character_uiyong_hp, potion):
    if potion[0] < 1:
        print("포션이 없습니다.")
        pass
    else:
        character_uiyong_hp[4] = character_uiyong_hp[5]
        print(f'🍖🥩포션을 먹고 초코의용의 체력이', character_uiyong_hp[4], '으로 만땅 충전되었습니다.🥩🍖')
        potion[0] -= 1
        # 김명은
        # for i in range(100):
        print(f'🥗포션', potion[0], '개가 남았습니다.🥗')
        print(f'🍋엘릭서', potion[1], '개가 남았습니다.🍋')
        # fight()


# 도망 확률 // 박규환 221209 1030
def escape_rate(esc_mob_lvl, esc_char_lvl):
    # 도망 확률 = 캐릭터 레벨 / 몬스터 레벨 + 캐릭터 레벨
    esc_rate = random.randint(1, esc_mob_lvl + esc_char_lvl)
    # 캐릭터 레벨과 랜덤값의 크기 비교 후
    if esc_rate <= esc_char_lvl:
        # 캐릭터 레벨이 높을 경우 1을 반환
        return 1
    else:
        # 아닐 경우 0을 반환
        return 0


# 몬스터의 능력치를 랜덤 설정 해주는 함수로 매개변수에는 monster_meet 함수 // 박규환 221208 1637
def monster_status(monster_status_a):
    # 몬스터의 정보를 임시로 저장해줄 리스트 선언
    monster_temp = []
    # 매개변수의 몬스터 정보를 temp 리스트 변수로 복사함
    monster_temp += monster_status_a
    # 최소 체력 = 최소 체력과 최대 체력 사이 랜덤값
    monster_temp[4] = random.randint(monster_temp[4], monster_temp[5])
    # 랜덤값을 최대 체력에도 적용해줌, 추후에 hp 최대치와 전투중 hp로 활용할 것을 상정
    monster_temp[5] = monster_temp[4]
    # 랜덤으로 부여된 체력 값에 따라 몬스터 레벨을 설정, 도주 or 추후 확장할 경우 강함을 척도로 사용하는 컨텐츠에 적용
    monster_temp[1] += int((monster_temp[4] - monster_status_a[4]) / (monster_status_a[5] - monster_status_a[4]) * 10)
    # 랜덤하게 설정된 능력치의 랜덤 몬스터 반환
    return monster_temp


# 조우한 몬스터를 랜덤으로 선정 // 박규환 221208 0926
def monster_meet():
    # 각 몬스터의 초기 설정된 hp, 공격력 등 스탯을 리스트에 만들어 저장
    character_zombie = ["좀비😈", 1, 100, 100, 300, 500, 48]
    character_ghoul = ["구울👾", 11, 180, 180, 450, 700, 30]
    character_skeleton = ["해골💀", 21, 220, 220, 480, 800, 12]
    character_bugbear = ["버그베어🐽", 31, 350, 350, 550, 900, 5]
    character_dongdong = ["동혀니😃", 41, 1000, 3000, 3000, 8000, 2]
    character_honghong = ["홍거리😆", 41, 1000, 3000, 3000, 8000, 2]
    character_diablo = ["디아복로👹", 71, 2500, 8000, 5000, 15000, 1]
    # 함수 내 반복문에 사용하기 위해 리스트에 담음
    character_monster = [character_zombie, character_ghoul, character_skeleton, character_bugbear, character_dongdong,
                         character_honghong, character_diablo]
    # 몬스터를 만날 확률의 총합을 합산할 변수 선언
    monster_meet_per = 0
    # 설정된 몬스터 종류 수만큼 반복
    for monster_meet_i in range(len(character_monster)):
        # 만날 확률을 합산
        monster_meet_per += character_monster[monster_meet_i][6]
    # 1부터 만날 확률을 합산한 값 사이의 랜덤한 숫자를 산출
    monster_meet_ran = random.randint(1, monster_meet_per)
    # 몬스터 판정을 위한 반복문
    for monster_meet_j in range(len(character_monster)):
        # 랜덤 숫자가 몬스터 고유 확률값보다 작거나 같을 시 해당 몬스터가 선택됨
        if monster_meet_ran <= character_monster[monster_meet_j][6]:
            # 선택한 몬스터를 반환
            return character_monster[monster_meet_j]
        # 아닐 경우
        else:
            # 총합에서 몬스터의 확률을 빼서 해당 배제
            monster_meet_ran -= character_monster[monster_meet_j][6]


# hp바 표시, 전투중인 캐릭터의 리스트를 인수로 대입 // 박규환 221209 1200
def hp_rate(character_hp):
    # hp가 차있는 값을 십분위로 변환
    hp_bar_recent = character_hp[4] / character_hp[5] * 10
    # hp가 0보다 작은 경우
    if character_hp[4] <= 0:
        # 지나치게 많은 깨진 하트가 출력되는 것을 막기 위해 hp를 0으로 변경해줌
        character_hp[4] = 0
        # 깨진 하트 10개를 출력, 오브젝트의 현재 / 최대 hp 출력
        print(10 * "\U0001F494", f"{character_hp[0]}HP: {character_hp[4]} / {character_hp[5]}")
    # 정상적인 경우
    else:
        # 10개의 하트 중 hp가 차있는 만큼의 온전한 하트 + hp가 깎인 만큼의 깨진 하트를 출력
        print(int(hp_bar_recent) * "\U0001F496" + (10 - int(hp_bar_recent)) * "\U0001F494",
              f"{character_hp[0]}HP: {character_hp[4]} / {character_hp[5]}")


# 몬스터 싸움 함수 고연재
def vs(ch_monster, uy, potion):

    print(f"{ch_monster[0]} 공격력 {ch_monster[2]} ~ {ch_monster[3]} 체력 {ch_monster[4]}출현!")  # 몬스터 랜덤으로 출현
    elixir_status = 0
    while True:  # 싸움 반복문 열기
        print(f"{uy[0]}: {uy[4]} // 포션: {potion[0]}, 엘릭서: {potion[1]}")
        print("1.공격 2.도망 3.물약 / 셋 중 하나를 선택하십시오:")  # 공격하거나 도망가거나 선택하는 인풋
        time.sleep(0.1)
        if key_board_battle() == '1':  # 공격을 선택했을때
            print(f"{uy[0]}이 {ch_monster[0]}를 공격했습니다.")  # 의용이가 랜덤의 몬스터를 공격한다.
            attack = random.randint(uy[2], uy[3])  # 공격 랜덤함수
            if ch_monster[4] <= attack:
                print(f"{ch_monster[0]}의 체력이 {ch_monster[4]}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
            else:
                print(f"{ch_monster[0]}의 체력이 {attack}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
            ch_monster[4] -= attack
            hp_rate(ch_monster)

            if ch_monster[4] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print("-" * 50)
                print(f"{uy[0]}의 승리입니다.")
                uy[5] += int((uy[5] * 0.05))  # 의용이 체력 5% 상승 / 최대체력
                uy[2] += int((uy[2] * 0.05))  # 의용이 최소 공격력 5% 상승
                uy[3] += int((uy[3] * 0.05))  # 의용이 최대 공격력 5% 상승
                uy[1] += 1
                if ch_monster[0] == "디아복로👹":
                    print(f"{uy[0]}이 {ch_monster[0]}을 물리치고 세상을 구했습니다.")
                    exit()
                print(f"{uy[0]}의 레벨:{uy[1]}\n{uy[0]}의 최대체력:{uy[5]}\n{uy[0]}의 최소공격력:{uy[2]}\n"
                      f"{uy[0]}의 최대공격력:{uy[3]}")
                break

            print("-" * 50)

            print(f"{ch_monster[0]}이 {uy[0]}을 공격했습니다.")  # 몬스터가 의용이를 공격
            mon_attack = random.randint(ch_monster[2], ch_monster[3])  # 몬스터의 최소 공격 최대 공격 만큼 랜덤함수 돌림
            ch_monster[2] = mon_attack  # 몬스터의 공격력 랜덤값만큼 설정
            if elixir_status == 0:
                if uy[4] <= ch_monster[2]:
                    print(f"{uy[0]}의 체력이 {uy[4]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                else:
                    print(f"{uy[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                uy[4] -= mon_attack  # 의용이 체력에서 몬스터 공격력만큼 빼줌
            else:
                print(f"엘릭서로 인한 무적 효과 발동중... 데미지를 입지 않습니다. {elixir_status - 1}턴 남음.")
                elixir_status -= 1
            hp_rate(uy)
            print("-" * 50)

            if ch_monster[4] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print("-" * 50)
                print(f"{uy[0]}의 승리입니다.")
                uy[5] += (uy[5] * 0.05)  # 의용이 체력 5% 상승 / 최대체력
                uy[2] += (uy[2] * 0.05)  # 의용이 최소 공격력 5% 상승
                uy[3] += (uy[3] * 0.05)  # 의용이 최대 공격력 5% 상승
                uy[1] += 1
                print(f"{uy[0]}의 레벨:{uy[1]}\n{uy[0]}의 최대체력:{uy[5]}\n{uy[0]}의 최소공격력:{uy[2]}\n"
                      f"{uy[0]}의 최대공격력:{uy[3]}")
                print("-" * 50)
                break
            elif uy[4] <= 0:
                print(f"{ch_monster[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
                exit()
        elif key_board_battle() == '2':
            print(f"{uy[0]}이 도망을 선택했습니다.")  # 도망 시나리오
            if escape_rate(ch_monster[1], uy[1]) == 1:  # 도망 성공
                print("도망가는데 성공했습니다.")
                return ch_monster
            else:  # 도망 실패
                print("도망가는데 실패했습니다.")
                print(f"{ch_monster[0]}이 {uy[0]}을 공격했습니다.")  # 몬스터가 의용이를 공격
                mon_attack = random.randint(ch_monster[2], ch_monster[3])  # 몬스터의 최소 공격 최대 공격 만큼 랜덤함수 돌림
                ch_monster[2] = mon_attack  # 몬스터의 공격력 랜덤값만큼 설정
                if elixir_status == 0:
                    if uy[4] <= ch_monster[2]:
                        print(f"{uy[0]}의 체력이 {uy[4]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                    else:
                        print(f"{uy[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                    uy[4] -= mon_attack  # 의용이 체력에서 몬스터 공격력만큼 빼줌
                else:
                    print(f"엘릭서로 인한 무적 효과 발동중... 데미지를 입지 않습니다. {elixir_status - 1}턴 남음.")
                    elixir_status -= 1
                hp_rate(uy)
                print("-" * 50)
                if uy[4] <= 0:
                    print(f"{ch_monster[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
                    exit()
                else:
                    continue
        elif key_board_battle() == '3':
            print("1. 포션 2. 엘릭서")
            time.sleep(0.1)
            if key_board_battle() == '1':
                water_medicine_drink(uy, potion)
                continue
            elif key_board_battle() == '2':
                elixir_status = elixir(uy, potion)
            else:
                print("잘못된 입력입니다.")
        else:
            print("잘못된 입력입니다.")

# 여러 함수에서 쓰이는 변수들을 모은 함수
def main():
    # 초코의용의 상태창 최소공격력, 최대공격력, hp
    uy = ["초코의용😁", 1, 100, 150, 500, 500]
    # 몬스터 생성(0,1)과 겹치지 않게 하기위해 초기값 4로 설정. 층을 1로 설정하면movea,moveb때문에 포탈도 이동을 함
    floor_i = 4
    # 이 리스트를 이용해 몬스터, p값 생성, 맵의 초기 좌표가 (0,0)이므로 겹치지 않게 하기 위해 1부터 시작하게 하였음.
    compre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # 셔플을 주어 실행을 할떄마다 랜덤한 위치에 생성하도록 함
    random.shuffle(compre)
    # 앞에 것은 포션, 뒤에 것은 엘릭서
    potion = [0, 0]
    # 1층에대한 함수 호출
    while_arr(floor_i, compre, potion, uy)
    print("2층 맵을 시작합니다 ==========")
    # 층을 증가시키기 위한 증감식
    floor_i += 1
    # 2층에대한 함수 호출
    while_arr(floor_i, compre, potion, uy)
    print("3층 맵을 시작합니다 ==========")
    floor_i += 1
    # 3층에 대한 함수 호출
    while_arr(floor_i, compre, potion, uy)

# 1~3층이 들어가있는(while_arr)을 호출하기 위한 메인함수 호출
main()
