import random
import keyboard as keyboard
import time

class party:
    def __init__(self,win,potion,elix):
        self.attack1 = None
        self.attack2 = None
        self.attack3 = None
        self.attack4 = None
        self.hp1 = None
        self.hp2 = None
        self.hp3 = None
        self.hp4 = None
        self.mp1 = None
        self.mp2 = None
        self.mp3 = None
        self.mp4 = None
        self.potion = potion
        self.elix = elix
        self.win = win
        self.rand = random.randrange(2,6)
    def party1(self):
        self.attack1 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp1 = round(500 * ((self.win * self.rand/100)+1))
        self.mp1 = round(300 * ((self.win * self.rand/100)+1))
        return ["의용군",self.attack1, self.hp1, self.mp1]
    def party2(self):
        self.attack2 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp2 = round(500 * ((self.win * self.rand/100)+1))
        self.mp2 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack2, self.hp2, self.mp2
    def party3(self):
        self.attack3 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp3 = round(500 * ((self.win * self.rand/100)+1))
        self.mp3 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack3, self.hp3, self.mp3
    def party4(self):
        self.attack4 = round(random.randrange(101,151) * ((self.win * self.rand/100)+1))
        self.hp4 = round(500 * ((self.win * self.rand/100)+1))
        self.mp4 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack4, self.hp4, self.mp4
    def inven(self):
        return self.potion, self.elix

class mapinfo:
    def __init__(self):
        self.rows = 16
        self.cols = 16
    def maping(self,):                                       #맵 기조 배열 생성
        return [[0 for j in range(self.cols)] for i in range(self.rows)]
    def rand(self):                                                   #배열내 랜덤좌표값
        randcol = random.randrange(0, 15)
        randrow = random.randrange(0, 15)
        return randcol, randrow
    def rand2(self):                                                  #1~100까지 랜덤값
        return random.randrange(1, 101)
    def mapimg(self,map):                                             #심층 정보 토대로 콘솔 맵 출력
        for i in range(0,15):
            for j in range(0,15):
                if (map[i][j] == 0 or map[i][j]==10 or map[i][j]==11):
                    print("\033[37;47m⬜\033[0;38m",end="")
                if (map[i][j] == 1):
                    print("🤺",end="")
                if (map[i][j] == 2):
                    print("⬛",end="")
                if (map[i][j] == 3):
                    print("👾",end="")
                if (map[i][j] == 4):
                    print("🏴󠁧󠁢󠁷󠁬󠁳󠁿",end="")
            print("")
    def sight(self,map,col,row):                                       #시야
        for i in range (-1,2):
            for j in range (-1,2):
                if i==0 and j==0:
                    continue
                if col > 0 or col < 14 or row > 0 or row < 14:
                    if map[col+i][row+j] == 10:
                        map[col+i][row+j] = 3
                    elif map[col+i][row+j] == 11:
                        map[col+i][row+j] = 4
                    else:
                        map[col+i][row+j] = 2

def mob():
    moblist=['임시몹',100,500]
    return moblist

def battle(win):
    potion = elix = 0
    ch_monster=mob()
    partys=party(win,potion,elix)
    uy=partys.party1()
    potion, elix=partys.inven()
    print(f"{ch_monster[0]} 공격력 {ch_monster[1]} 체력 {ch_monster[2]}출현!")  # 몬스터 랜덤으로 출현
    elixir_status = 0
    while True:  # 싸움 반복문 열기
        print(f"{ch_monster[0]} 공격력 {ch_monster[1]} 체력 {ch_monster[2]}")
        print(f"{uy[0]}: {uy[1]}, {uy[2]} // 포션: {potion}, 엘릭서: {elix}")
        print("1.공격 2.도망 3.물약 / 셋 중 하나를 선택하십시오:")  # 공격하거나 도망가거나 선택하는 인풋
        select=int(input())
        if select == 1:  # 공격을 선택했을때
            print(f"{uy[0]}이 {ch_monster[0]}를 공격했습니다.")  # 의용이가 랜덤의 몬스터를 공격한다.
            if ch_monster[2] <= uy[1]:
                print(f"{ch_monster[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
            else:
                print(f"{ch_monster[0]}의 체력이 {uy[1]}만큼 줄었습니다.")  # 몬스터 피가 공격력만큼 줄어듦
            ch_monster[2] -= uy[1]
            print(ch_monster[2],"남음")

            if ch_monster[2] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print("-" * 50)
                print(f"{uy[0]}의 승리입니다.")
                win += 1
                if ch_monster[0] == "디아복로👹":
                    print(f"{uy[0]}이 {ch_monster[0]}을 물리치고 세상을 구했습니다.")
                    exit()
                print(f"{uy[0]}의 레벨:{win}\n{uy[0]}의 \n{uy[0]}의 공격력:{uy[1]}\n")
                break

            print("-" * 50)

            print(f"{ch_monster[0]}이 {uy[0]}을 공격했습니다.")  # 몬스터가 의용이를 공격
            if elixir_status == 0:
                if uy[2] <= ch_monster[2]:
                    print(f"{uy[0]}의 체력이 {uy[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                else:
                    print(f"{uy[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                uy[2] -= ch_monster[1]  # 의용이 체력에서 몬스터 공격력만큼 빼줌
            else:
                print(f"엘릭서로 인한 무적 효과 발동중... 데미지를 입지 않습니다. {elixir_status - 1}턴 남음.")
                elixir_status -= 1
            print("-" * 50)

            if ch_monster[2] <= 0:  # 몬스터 체력이 0에 수렴하면 의용이의 승리
                print("-" * 50)
                print(f"{uy[0]}의 승리입니다.")
                win += 1
                print(f"{uy[0]}의 레벨:{win}\n")
                print("-" * 50)
                return win
            elif uy[2] <= 0:
                print(f"{ch_monster[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
                exit()
        elif select == 2:
            print(f"{uy[0]}이 도망을 선택했습니다.")  # 도망 시나리오
            escape_rate=random.randrange(1,101)
            if escape_rate <= 10:  # 도망 성공
                print("도망가는데 성공했습니다.")
                return ch_monster
            else:  # 도망 실패
                print("도망가는데 실패했습니다.")
                print(f"{ch_monster[0]}이 {uy[0]}을 공격했습니다.")  # 몬스터가 의용이를 공격
                if elixir_status == 0:
                    if uy[2] <= ch_monster[2]:
                        print(f"{uy[0]}의 체력이 {uy[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                    else:
                        print(f"{uy[0]}의 체력이 {ch_monster[2]}만큼 줄었습니다.")  # 의용이 피가 공격력만큼 줄어듦
                    uy[2] -= ch_monster[1]  # 의용이 체력에서 몬스터 공격력만큼 빼줌
                else:
                    print(f"엘릭서로 인한 무적 효과 발동중... 데미지를 입지 않습니다. {elixir_status - 1}턴 남음.")
                    elixir_status -= 1
                print(uy[1],"남음")
                print("-" * 50)
                if uy[2] <= 0:
                    print(f"{ch_monster[0]}(이)가 이겼습니다.\n 게임오버....")  # 몬스터가 이기면 게임 끝
                    exit()
                else:
                    continue
        elif select == 3:
            print("1. 포션 2. 엘릭서")
            select2=int(input())
            if select2 == 1:
                potion-=1
                continue
            elif select2 == 2:
                elixir_status += 10
                elix-=1
            else:
                print("잘못된 입력입니다.")
        else:
            print("잘못된 입력입니다.")

def map():                                                              #맵총괄함수
    col=0
    win=0
    row=0
    step=0
    colrow = []
    floor = 1
    floorcnt=1
    battlecnt=0

    while (1):
        dummy = mapinfo()                                               #클래스 사용을 위해 더미변수에 담음
        map = dummy.maping()
        potionrand=dummy.rand2()                                        #rand2클래스에서 랜덤값 받아옴

        for j in range (0,16):                                          #오류있어서 안보이는 16번째줄 배열만듬
            map[j][15]=99

        if potionrand<=4:
            print("이동중 포션 드랍")

        if(battlecnt/10==1 or step==0):                                 #몬스터 갱신
            print("갱신")
            colrow = []
            battlecnt=0
            for i in range(0,21):
                randcol,randrow=dummy.rand()
                colrow.append(randcol)
                colrow.append(randrow)

        for i in range (0,39,2):
            map[colrow[i]][colrow[i+1]] = 10                            #몬스터 위장
            if floor<5:
                map[colrow[40]][colrow[41]] = 11                        #포탈 위장

        if floorcnt==1:                                                 #층오름 변수가 1이되면 유저위치를 재배치 한 뒤 0으로변경
            col,row=dummy.rand()
            floorcnt=0
        map[col][row]=1

        print("발걸음수",step)
        print("%d층"%floor)
        print("%d회 전투함"%battlecnt)

        dummy.sight(map,col,row)                                        #시야
        dummy.mapimg(map)                                               #맵 이미지 출력,인자를 위에서 받은 map을 넣어줌

        select = keyboard.read_key()                                    #방향키 입력받음
        time.sleep(0.3)
        if select=='left':
            if (row < 1):
                continue
            else:
                map[col][row] = 0
                row-=1
                map[col][row-1] = 1
        elif select == 'down':
            if (col > 13):
                continue
            else:
                map[col][row] = 0
                col+=1
                map[col+1][row] = 1
        elif select == 'right':
            if (row > 13):
                continue
            else:
                map[col][row] = 0
                row+=1
                map[col][row+1] = 1
        elif select == 'up':
            if (col < 1):
                continue
            else:
                map[col][row] = 0
                col-=1
                map[col-1][row] = 1

        step+=1                                                            #발걸음수 증가

        if map[col][row] == 3:                                             #몬스터 만나면 전투
            battlecnt+=1
            battle(win)
            win+=1
            if win==1:
                for i in range(0, 39, 2):
                    if colrow[i]==col and colrow[i+1]==row:
                        colrow[i]=15
                        colrow[i+1]=15

        elif map[col][row] == 4:                                           #포탈 만나면 다음층이동,발걸음,전투카운트 초기화
            floor+=1
            floorcnt=1
            battlecnt=0
            step=0
map()