import random


class Player:  # 플레이어 클래스
    def __init__(self, name):  # 생성자
        # 파티원 전체 공통 사항은 Player에서 정의
        self.name = name  # 이름
        self.minDmg = 100  # 최소 대미지
        self.maxDmg = 150  # 최대 대미지
        self.maxHp = 500  # 최대 체력
        self.hp = self.maxHp  # 현재 체력
        self.maxMp = 300  # 최대 마나
        self.mp = self.maxMp  # 현재 마나
        self.state = '대기'  # 대기: 아직 공격을 하지 않은 상태, 완료: 공격을 마친 상태, 전투불능: 기절 상태

    def view_stat(self):  # 정보 출력 함수
        print(f"이름: {self.name}")
        print(f"공격력: {self.minDmg} ~ {self.maxDmg}")
        print(f"현재 / 최대 마나: {self.mp} / {self.maxMp}")
        print(f"현재 / 최대 체력: {self.hp} / {self.maxHp}")


class Warrior(Player):  # Player 클래스 상속받음
    def __init__(self, name):
        super().__init__(name)  # Player 클래스의 생성자 상속받음
        self.skill = {'초코 쉴드': Skill('초코쉴드', 0),
                      '불꽃 초코 의지': Skill('불꽃초코의지', 0),
                      '초코에몽 반사': Skill('초코에몽 반사', 0)}

    def use_skill(self, num):  # 대충 스킬 사용 함수, 미구현
        if num == 1:
            if self.mp >= self.skill['초코 쉴드'].mana:
                print("초코 쉴드 스킬 사용")
                self.mp -= self.skill['초코 쉴드'].mana


class Bard(Player):
    def __init__(self, name):
        super().__init__(name)
        self.skill = {'골목대장 킹기태': Skill('골목대장 킹기태', 0),
                      '보컬 트레이닝': Skill('보컬 트레이닝', 0),
                      '기태 쉿': Skill('기태 쉿', 0)}

    def use_skill(self, num):
        if num == 1:
            if self.mp >= self.skill['골목대장 킹기태'].mana:
                print("골목대장 킹기태 스킬 사용")
                self.mp -= self.skill['골목대장 킹기태'].mana


class MediFighter(Player):
    def __init__(self, name):
        super().__init__(name)
        self.skill = {'포션 제조': Skill('포션 제조', 0),
                      '자양강장제 제조': Skill('자양강장제 제조', 0),
                      '약병 투척': Skill('약병 투척', 0)}

    def use_skill(self, num):
        if num == 1:
            if self.mp >= self.skill['포션 제조'].mana:
                print("포션 제조 스킬 사용")
                self.mp -= self.skill['포션 제조'].mana


class Ranger(Player):
    def __init__(self, name):
        super().__init__(name)
        self.skill = {'연재 화살': Skill('연재 화살', 0),
                      '연속 화살': Skill('연속 화살', 0),
                      '독화살': Skill('독화살', 0)}

    def use_skill(self, num):
        if num == 1:
            if self.mp >= self.skill['연재 화살'].mana:
                print("연재 화살 스킬 사용")
                self.mp -= self.skill['연재 화살'].mana


class Skill:  # 스킬 클래스
    def __init__(self, name, mana):
        self.name = name  # 스킬 이름
        self.mana = mana  # 마나 소모량
        # 이 아래로 필요한 사항 더 추가하며 사용할 것


class Mob:  # 몬스터 클래스
    def __init__(self, name, minDmg, maxDmg, minHp, maxHp, isSix=False):  # 생성자
        self.name = name  # 이름
        self.minDmg = minDmg  # 최소 대미지
        self.maxDmg = maxDmg  # 최대 대미지
        self.minHp = minHp  # 최소 체력
        self.maxHp = maxHp  # 최대 체력
        self.hp = 0  # 현재 체력, 나중에 최소 체력 ~ 최대 체력에서 랜덤으로 들어감
        self.debuff = None  # 플레이어의 스킬로 인한 디버프 상태
        self.isSix = isSix  # 6인부대장 & 디아복로 판별 변수
        self.isAlive = True  # 처치 상태, 6인부대장 & 디아복로에게만 해당 True:살아있음, False:처치함

    def view_stat(self):  # 정보 출력 함수
        print(f"이름: {self.name}")
        print(f"공격력: {self.minDmg} ~ {self.maxDmg}")
        print(f"현재 / 최대 체력: {self.hp} / {self.maxHp}")


class Item:  # 아이템 클래스
    def __init__(self, name):
        self.name = name  # 이름
        # 이 아래로 필요한 사항 추가하며 사용할 것


def create_mobs():  # 메인 함수에 넘겨줄 몬스터 딕셔너리
    # 이름, 최소공격력, 최대공격력, 최소체력, 최대체력, (6인부대장일 때만 True 추가)
    mobs = {'좀비': Mob('좀비', 100, 100, 300, 500), '구울': Mob('구울', 180, 180, 450, 700),
            '해골': Mob('해골', 220, 220, 480, 800), '버그베어': Mob('버그베어', 350, 350, 550, 900),
            '아르헨도': Mob('아르헨도', 1000, 3000, 5000, 10000, True), '철몸': Mob('철몸', 1000, 3000, 5000, 10000, True),
            '규범이': Mob('규범이', 1000, 3000, 5000, 10000, True), '민주석': Mob('민주석', 1000, 3000, 5000, 10000, True),
            '일성김': Mob('일성김', 1000, 3000, 5000, 10000, True), '우연이': Mob('우연이', 1000, 3000, 5000, 10000, True),
            '디아복로': Mob('디아복로', 2500, 8000, 10000, 20000, True)}
    return mobs


def create_players():  # 메인 함수에 넘겨줄 플레이어 딕셔너리
    players = {'초코의용군': Warrior('초코의용군'),
               '킹기태': Player('킹기태'),
               '약범규': Player('약범규'),
               '보우연재': Player('보우연재')}
    return players


def create_items():  # 메인 함수에 넘겨줄 아이템 딕셔너리
    #
    items = {'포션': Item('포션'), '엘릭서': Item('엘릭서'),
             '그대와 함께라면': Item('그대와 함께라면')}
    return items


def level_up(players):  # 전투 승리 후 스탯 증가
    for i in players:
        per = random.randint(2, 5)  # 2~5 퍼센트 랜덤
        print(f"'{players[i].name}'의 스탯이 {per}%만큼 증가합니다\n")
        # players['초코의용군'].name == players[i].name
        players[i].view_stat()  # 스탯 출력 함수

        players[i].maxHp += round(players[i].maxHp * (per / 100))
        players[i].maxMp += round(players[i].maxMp * (per / 100))

        if players[i].state == '전투불능':  # 전투 불능일 땐 스탯은 증가시키되 현재 체력 및 마나는 절반만 회복
            players[i].hp = players[i].maxHp / 2
            players[i].mp = players[i].maxMp / 2

        else:  # 전투불능 아니면 원래대로
            players[i].hp = players[i].maxHp
            players[i].mp = players[i].maxMp

        players[i].minDmg += round(players[i].minDmg * (per / 100))
        players[i].maxDmg += round(players[i].maxDmg * (per / 100))

        print("\n↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓\n")

        players[i].view_stat()
        print("\n")


def main():
    players = create_players()  # players 딕셔너리 메인 함수로 가져옴
    items = create_items()  # items 딕셔너리 메인 함수로 가져옴
    mobs = create_mobs()  # mobs 딕셔너리 메인 함수로 가져옴

    # nowMob = mobs['디아복로']  # nowMob에 mobs 딕셔너리에 있던 디아복로를 저장
    # nowMob.hp = random.randint(nowMob.minHp, nowMob.maxHp)  # 몹의 hp는 전투 시작 시 최소~최대값 사이에서 랜덤으로 배정됨
    # print(nowMob.name)
    # print("nowMob:", nowMob.hp, "\tmobs['디아복로']", mobs['디아복로'].hp)
    # nowMob.hp -= 100
    # print("nowMob:", nowMob.hp, "\tmobs['디아복로']", mobs['디아복로'].hp)
    # print("nowMob:", nowMob.isAlive, "\tmobs['디아복로']", mobs['디아복로'].isAlive)

    # 맵에서 몬스터를 만났을 때
    # if nowMob.isSix:
    #     if nowMob.isAlive:
    #         # 전투 시작
    #     else:
    #         # 전투 스킵
    #         # 다른 몬스터 랜덤

    # 전투 승리 시
    # if nowMob.isSix:
    #     nowMob.isAlive = False  # 처치 시 isAlive를 False로 바꿔줌
    #
    # print("nowMob:", nowMob.isAlive, "\tmobs['디아복로']", mobs['디아복로'].isAlive)

    for i in players:
        print(players[i].name)
    print()
    for i in mobs:
        print(mobs[i].name)
    print()
    for i in items:
        print(items[i].name)


def mob_rand(mobs):  # 몬스터 결정 함수
    mobRand = random.randint(1, 1000)
    if mobRand <= 465:
        return mobs['좀비']
    if 465 < mobRand <= 765:
        return mobs['구울']
    if 765 < mobRand <= 885:
        return mobs['해골']
    if 885 < mobRand <= 935:
        return mobs['버그베어']
    if 935 < mobRand <= 945:
        return mobs['아르헨도']
    if 945 < mobRand <= 955:
        return mobs['철몸']
    if 955 < mobRand <= 965:
        return mobs['규범이']
    if 965 < mobRand <= 975:
        return mobs['민주석']
    if 975 < mobRand <= 985:
        return mobs['일성김']
    if 985 < mobRand <= 995:
        return mobs['우연이']
    if 995 < mobRand <= 1000:
        return mobs['디아복로']


main()
