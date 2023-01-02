import random


# 도망 확률
def escape_rate(esc_mob_lvl, esc_char_lvl):
    # 도망 확률 = 캐릭터 레벨 / 몬스터 레벨 + 캐릭터 레벨
    esc_rate = random.randint(1, esc_mob_lvl + esc_char_lvl)
    # 캐릭터 레벨이 랜덤값보다 높을 경우 참, 아니면 거짓
    if esc_rate <= esc_char_lvl:
        return 1
    else:
        return 0


# 몬스터의 능력치를 랜덤 설정 해주는 함수로 매개변수에는 monster_meet 함수
def monster_status(monster_status_a):
    monster_temp = []
    monster_temp += monster_status_a
    # 최소 체력과 최대 체력 사이 랜덤값
    monster_temp[4] = random.randint(monster_temp[4], monster_temp[5])
    monster_temp[5] = monster_temp[4]
    monster_temp[1] += int((monster_temp[4] - monster_status_a[4]) / (monster_status_a[5] - monster_status_a[4]) * 10)
    # print(f"{monster_temp[0]}(이)가 나타났습니다.")
    # 랜덤하게 설정된 능력치의 랜덤 몬스터 반환
    return monster_temp


# 매개변수에 character_monster 리스트, 조우한 몬스터를 랜덤으로 선정
def monster_meet():
    character_zombie = ["좀비😈", 1, 100, 100, 300, 500, 48]
    character_ghoul = ["구울👾", 11, 180, 180, 450, 700, 30]
    character_skeleton = ["해골💀", 21, 220, 220, 480, 800, 12]
    character_bugbear = ["버그베어🐽", 31, 350, 350, 550, 900, 5]
    character_dongdong = ["동혀니😃", 41, 1000, 3000, 3000, 8000, 2]
    character_honghong = ["홍거리😆", 41, 1000, 3000, 3000, 8000, 2]
    character_diablo = ["디아복로👹", 71, 2500, 8000, 5000, 15000, 1]
    character_monster = [character_zombie, character_ghoul, character_skeleton, character_bugbear, character_dongdong,
                         character_honghong, character_diablo]
    # 몬스터를 만날 확률의 총합을 합산할 변수 선언
    monster_meet_per = 0
    # 각각의 몬스터를 만날 확률을 합산하기 위한 반복문
    for monster_meet_i in range(len(character_monster)):
        monster_meet_per += character_monster[monster_meet_i][6]
    # 1부터 만날 확률을 합산한 값 사이의 랜덤한 숫자를 산출
    monster_meet_ran = random.randint(1, monster_meet_per)
    # 몬스터 판정을 위한 반복문
    for monster_meet_j in range(len(character_monster)):
        # 랜덤 숫자가 몬스터 고유 확률값보다 작거나 같을 시 해당 몬스터가 선택됨
        if monster_meet_ran <= character_monster[monster_meet_j][6]:
            return character_monster[monster_meet_j]
        # 아닐 경우 총합에서 몬스터의 확률을 빼서 해당 배제
        else:
            monster_meet_ran -= character_monster[monster_meet_j][6]


# hp바 표시, 전투중인 캐릭터의 리스트를 인수로 대입
def hp_rate(character_hp):
    # hp가 차있는 값을 십분위로 변환
    if character_hp[4] <= 0:
        character_hp[4] = 0
    else:
        pass
    hp_bar_recent = character_hp[4] / character_hp[5] * 10
    # 10개의 하트 중 hp가 차있는 만큼 + hp가 깎인 만큼 각각 다른 하트로 출력
    print(int(hp_bar_recent) * "\U0001F496" + (10 - int(hp_bar_recent)) * "\U0001F494",
          f"{character_hp[0]}HP: {character_hp[4]} / {character_hp[5]}")


def vs_attack(vs_character_1, vs_character_2, elixir_status):
    print("-" * 50)
    print(f"{vs_character_1[0]}이 {vs_character_2[0]}를 공격했습니다.")  # 의용이가 랜덤의 몬스터를 공격한다.
    attack = random.randint(vs_character_1[2], vs_character_1[3])  # 공격 랜덤함수
    if vs_character_2[0] == "초코의용😁" and elixir_status > 0:
        print(f"{vs_character_2[0]}은 엘릭서 복용 상태입니다. 체력이 줄어들지 않습니다.")
    else:
        print(f"{vs_character_2[0]}의 체력이 {attack}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
        vs_character_2[4] -= attack
    hp_rate(vs_character_2)
    print("-" * 50)
    return vs_character_2


def game_over(main_char, enemy_char):
    if main_char[4] <= 0:
        print(f"{enemy_char[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
        exit()


def vs_victory(main_char):
    main_char[5] += int((main_char[5] * 0.05))  # 의용이 체력 5% 상승 / 최대체력
    main_char[2] += int((main_char[2] * 0.05))  # 의용이 최소 공격력 5% 상승
    main_char[3] += int((main_char[3] * 0.05))  # 의용이 최대 공격력 5% 상승
    main_char[1] += 1
    print(f"{main_char[0]}의 레벨:{main_char[1]}\n{main_char[0]}의 최대체력:{main_char[5]}\n"
          f"{main_char[0]}의 최소공격력:{main_char[2]}\n{main_char[0]}의 최대공격력:{main_char[3]}")
    return main_char


def vs_opening(vs_monster_meet):
    print(f"{vs_monster_meet[0]}출현!")  # 몬스터 랜덤으로 출현


def escape_process(escape_char, escape_enemy, escape_elixir):
    print(f"{escape_char[0]}이 도망을 선택했습니다.")  # 도망 시나리오
    if escape_rate(escape_enemy[1], escape_char[1]) == 1:  # 도망 성공
        print("도망가는데 성공했습니다.")
        return 1
    else:  # 도망 실패
        print("도망가는데 실패했습니다.")
        uy = vs_attack(escape_enemy, escape_char, escape_elixir)
        game_over(escape_char, escape_enemy)
        return 0


def battle_get_potion(battle_get_potion_a):  # potion을 매개변수로 사용
    if random.randint(1, 2) == 1:  # 랜덤 2가지로 50% 확률
        if random.randint(1, 200) == 1:  # 0.5%의 랜덤확률로
            battle_get_potion_a[1] += 1  # elixir 갯수 +1
        else:
            battle_get_potion_a[0] += 1  # potion 갯수 +1개
    else:
        pass
    return battle_get_potion_a


def use_potion(potion_char, potion_quantity):
    if potion_quantity[0] == 0:
        print("포션이 없습니다.")
    else:
        print(f"{potion_char[0]}의 체력이 회복됩니다.")
        potion_char[4] = potion_char[5]
        potion_quantity[0] -= 1
        return potion_quantity[0]


def use_elixir(elixir_char, elixir_quantity):
    if elixir_quantity[1] == 0:
        print("엘릭서가 없습니다.")
    else:
        print(f"{elixir_char[0]}(이)가 무적 상태에 돌입합니다.")
        return 10


# 몬스터 싸움 함수
def vs(ch_monster, uy, potion):
    # 초코의용 상태창 리스트는 성빈이 함수로 옮길 예정
    elixir_usage = 0
    vs_opening(ch_monster)
    while True:  # 싸움 반복문 열기
        print(f"현재 도구 보유 상황: 포션{potion[0]}개, 엘릭서{potion[1]}개")
        command = int(input("1.공격 2.도망 3.도구"))  # 공격을 선택했을때
        if command == 1:
            ch_monster = vs_attack(uy, ch_monster, elixir_usage)
            if ch_monster[4] > 0:
                uy = vs_attack(ch_monster, uy, elixir_usage)
            else:
                pass
            if ch_monster[4] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print(f"{uy[0]}의 승리입니다.")
                uy = vs_victory(uy)
                battle_get_potion(potion)
                break
            game_over(uy, ch_monster)
        elif command == 3:
            if int(input("1, 포션, 2. 엘릭서")) == 1:
                use_potion(uy, potion)
            else:
                elixir_usage = use_elixir(uy, potion)
                potion[1] -= 1
                if potion[1] < 0:
                    potion[1] = 0
                else:
                    pass
        else:
            if escape_process(uy, ch_monster, elixir_usage) == 1:
                break
            else:
                pass
        if elixir_usage > 0:
            print(f"엘릭서 복용 상태입니다. {elixir_usage}턴 남았습니다.")
            elixir_usage -= 1
        else:
            pass
    return uy


def main_func():
    uy_main = ["초코의용😁", 1, 100, 150, 500, 500]  # 초코의용 리스트 이름/최소공격력/최대공격력/최소 체력/최대 체력
    potion_main = [100, 10]
    for i in range(500):
        uy_main = vs(monster_status(monster_meet()), uy_main, potion_main)


main_func()
