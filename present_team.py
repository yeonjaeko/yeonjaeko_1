import random
import keyboard as keyboard
import time

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
class party:
    def __init__(self,potion,elix,ramen,stat1,stat2,stat3,stat4):
        self.potion = potion
        self.elix = elix
        self.ramen = ramen
        self.rand = random.randrange(2, 6)
        self.attack1 = stat1[0]
        self.attack11 = stat1[1]
        self.hp1 = stat1[2]
        self.mp1 = stat1[3]
        self.attack2 = stat2[0]
        self.attack22 = stat2[1]
        self.hp2 = stat2[2]
        self.mp2 = stat2[3]
        self.attack3 = stat3[0]
        self.attack33 = stat3[1]
        self.hp3 = stat3[2]
        self.mp3 = stat3[3]
        self.attack4 = stat4[0]
        self.attack44 = stat4[1]
        self.hp4 = stat4[2]
        self.mp4 = stat4[3]

    def party1(self):
        attack1 = 100+self.attack1
        attack11 = 150 + self.attack11
        hp1 = 500 + self.hp1
        mp1 = 300 + self.mp1
        dead = False

        return ["초코의용군",attack1, attack11, hp1, mp1,dead]
    def party2(self):
        attack2= 100 + self.attack2
        attack22 = 150 + self.attack22
        hp2 = 500 + self.hp2
        mp2 = 300 + self.mp2
        dead = False


        return ["킹기태",attack2, attack22, hp2, mp2,dead]
    def party3(self):
        attack3 = 100 + self.attack3
        attack33 = 150 + self.attack33
        hp3 = 500 + self.hp3
        mp3 = 300 + self.mp3
        dead = False

        return ["약범규",attack3, attack33, hp3, mp3,dead]
    def party4(self):
        attack4 = 100 + self.attack4
        attack44 = 150 + self.attack4
        hp4 = 500 + self.hp4
        mp4 = 300 + self.mp4
        dead = False

        return ["보우연재",attack4, attack44, hp4, mp4,dead]
    def inven(self):
        return self.potion, self.elix, self.ramen



class Mon_Status:
    boss_kill_list = [0, 0, 0, 0, 0, 0, 0]

    def Diablo(self):
        self.name = '디아복로👹'
        self.attack = random.randrange(1000, 1001)
        self.hp = random.randrange(1000, 5000)
        return [self.name, self.attack, self.hp]

    def Wuyeon(self):
        self.name = '우연🤨'
        self.attack = random.randrange(1, 31)
        self.hp = random.randrange(5, 11)
        return [self.name, self.attack, self.hp]

    def Ilsungkim(self):
        self.name = '일성킴👺'
        self.attack = random.randrange(1, 31)
        self.hp = random.randrange(5, 11)
        return [self.name, self.attack, self.hp]

    def MinJuSeok(self):
        self.name = '민주석😏'
        self.attack = random.randrange(1, 31)
        self.hp = random.randrange(5, 11)
        return [self.name, self.attack, self.hp]

    def KyuBeom(self):
        self.name = '규범👽'
        self.attack = random.randrange(1, 31)
        self.hp = random.randrange(5, 11)
        return [self.name, self.attack, self.hp]

    def ChulMoom(self):
        self.name = '철몸😾'
        self.attack = random.randrange(1, 31)
        self.hp = random.randrange(5, 11)
        return [self.name, self.attack, self.hp]

    def Ado(self):
        self.name = '아르헨도⚽'
        self.attack = random.randrange(1, 31)
        self.hp = random.randrange(5, 11)
        return [self.name, self.attack, self.hp]


    def BugBear(self):
        self.name = '버그베어👾'
        self.attack = random.randrange(350, 351)
        self.hp = random.randrange(550, 901)
        return [self.name, self.attack, self.hp]

    def Skull(self):
        self.name = '해골💀'
        self.attack = random.randrange(220, 221)
        self.hp = random.randrange(480, 801)
        return [self.name, self.attack, self.hp]

    def Gull(self):
        self.name = '구울🤢'
        self.attack = random.randrange(180, 181)
        self.hp = random.randrange(450, 701)
        return [self.name, self.attack, self.hp]

    def Zombie(self):
        self.name = '좀비😈'
        self.attack = random.randrange(100, 101)
        self.hp = random.randrange(300, 501)
        return [self.name, self.attack, self.hp]

def Mon_Per():

    a = random.randrange(1, 71)
    number = a
    MON = Mon_Status()
    if number <= 70:
        return MON.Diablo()
    # elif 11 <= number <= 20:
    #     return MON.Wuyeon()
    # elif 21 <= number <= 30:
    #     return MON.Ilsungkim()
    # elif 31 <= number <= 40:
    #     return MON.MinJuSeok()
    # elif 41 <= number <= 50:
    #     return MON.KyuBeom()
    # elif 51 <= number <= 60:
    #     return MON.ChulMoom()
    # elif 61 <= number <= 70:
    #     return MON.Ado()
    # elif 63 <= number <= 102:
    #     return MON.BugBear()
    # elif 103 <= number <= 122:
    #     return MON.Skull()
    # elif 123 <= number <= 422:
    #     return MON.Gull()
    # else:
    #     return MON.Zombie()



class skill:
    def __init__(self,party1,party2,party3,party4):
        self.party1 = party1
        self.party2 = party2
        self.party3 = party3
        self.party4 = party4

    def skill1(self,mobhp):
        print("초코의용군 스킬1:현재체력비례20%")
        return [[mobhp-mobhp*0.2,3],1]

    def skill2(self,hpmax):
        print("초코의용군 스킬2:풀회복",hpmax)
        return [hpmax,2]

    def skill3(self,mobhp):
        print("초코의용군 스킬3:현재체력비례40%")
        return [mobhp-mobhp*0.4,3]

    def skill4(self, mobhp):
        print("킹기태 스킬1:현재체력비례10%")
        return [mobhp-mobhp*0.1,1]

    def skill5(self, hpmax):
        print("킹기태 스킬2:풀회복")
        return [hpmax,2]

    def skill6(self, mobhp):
        print("킹기태 스킬3:아군30%회복(최종치 초과가능)")
        return [round(self.party1[3]*0.3),round(self.party2[3]*0.3),round(self.party3[3]*0.3),round(self.party4[3]*0.3),3]

    def skill7(self, mobhp):
        print("약범규 스킬1:고정데미지1000")
        return [1000,1]

    def skill8(self,hpmax):
        print("약범규 스킬2:풀회복")
        return [hpmax,2]

    def skill9(self, mobhp):
        print("약범규 스킬3:라면제조")
        return [2,3]

    def skill10(self, mobhp):
        print("보우연재 스킬1:고정데미지4000")
        return [4000,1]

    def skill11(self, hpmax):
        print("보우연재 스킬2:풀회복")
        return [hpmax,2]

    def skill12(self, mobhp):
        print("보우연재 스킬3:상대와 자신 현재 체력비례 1~100%")
        return [round(self.party4[3]-self.party4[3]*(random.randrange(1,101)/100)),round(mobhp-mobhp*(random.randrange(1,101)/100)),3]

def skillcheck(num,win,potion,elix,ramen,mon,stat1,stat2,stat3,stat4):                                    #인자생성에 필요한 win,포션,엘릭서와구분을 위한 num값,계산을위한mob값
    partys=party(potion,elix,ramen,stat1,stat2,stat3,stat4)                                           #파티정보 받아오기위한준비
    allskill = skill(partys.party1(),partys.party2(),partys.party3(),partys.party4())
    partys2=partys.party1()
    if num==1:
        print("초코의용군 스킬,1,2,3")
        select=int(input())                      #제안:1번은 다 공격스킬, 2번은 회복스킬
        if select==1:
            return allskill.skill1(mon[2])
        if select==2:
            return allskill.skill2(partys2[3])
        if select==3:
            return allskill.skill3(mon[2])
    if num==2:
        print("킹기태 스킬,1,2,3")
        select = int(input())
        if select == 1:
            return allskill.skill4(mon[2])
        if select == 2:
            return allskill.skill5(partys2[3])
        if select == 3:
            return allskill.skill6(mon[2])
    if num==3:
        print("약범규 스킬,1,2,3")
        select = int(input())
        if select == 1:
            return allskill.skill7(mon[2])
        if select == 2:
            return allskill.skill8(partys2[3])
        if select == 3:
            return allskill.skill9(mon[2])
    if num==4:
        print("보우연재 스킬,1,2,3")
        select = int(input())
        if select == 1:
            return allskill.skill10(mon[2])
        if select == 2:
            return allskill.skill11(partys2[3])
        if select == 3:
            return allskill.skill12(mon[2])

def printstat(mon,uy,king,yak,bow,potion,elix,ramen):

    print("")
    print(f"{uy[0]} 최소 공격력:{uy[1]} 최대 공격력:{uy[2]} 체력:{uy[3]} 마력:{uy[4]} // 포션:{potion} 엘릭서:{elix} 라면:{ramen}")
    print("")
    print(f"{king[0]} 최소 공격력:{king[1]} 최대 공격력:{king[2]} 체력:{king[3]} 마력:{king[4]} // 포션:{potion} 엘릭서:{elix} 라면:{ramen}")
    print("")
    print(f"{yak[0]} 최소 공격력:{yak[1]} 최대 공격력:{yak[2]} 체력:{yak[3]} 마력:{yak[4]} // 포션:{potion} 엘릭서:{elix} 라면:{ramen}")
    print("")
    print(f"{bow[0]} 최소 공격력:{bow[1]} 최대 공격력:{bow[2]} 체력:{bow[3]} 마력:{bow[4]} // 포션:{potion} 엘릭서:{elix} 라면:{ramen}")
    print("")
    print("")

def battle(win,potion,elix,ramen, stat1,stat2,stat3,stat4):
    Mon_Status.boss_kill_list
    mon = Mon_Per()
    partys=party(potion, elix, ramen,stat1,stat2,stat3,stat4)
    uy = partys.party1()
    king = partys.party2()
    yak = partys.party3()
    bow = partys.party4()
    hpmax1 = uy[2]
    hpmax2 = king[2]
    hpmax3 = yak[2]
    hpmax4 = bow[2]
    mpmax1 = uy[3]
    mpmax2 = king[3]
    mpmax3 = yak[3]
    mpmax4 = bow[3]
    players = [uy, king, yak, bow]
    print(f"{mon[0]} 출현!!")
    elix_status = 0
    ramenturn = 0
    while True:
        if uy[3] <= 0:
            pass
        elif uy[3] >= 0:
                printstat(mon, uy, king, yak, bow, potion, elix, ramen)
                playercheck=1
                #의용군 파티가 몬스터를 공격
                print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
                print("남은 엘릭서 턴:",elix_status)
                select = int(input())

                if select == 1:
                    print(f"{uy[0]}이 {mon[0]}(를)을 공격했습니다.")
                    print("")

                    if mon[2] >= 0:
                        atk_uy = random.randint(uy[1], uy[2]+1)
                        print(f"{mon[0]}의 체력이 {atk_uy}만큼 줄었습니다.")
                        mon[2] -= atk_uy
                        print("")
                        print(f"현재 몬스터 체력:{mon[2]}")

                elif select == 2:                                                           #스킬
                    skill = skillcheck(playercheck, win, potion, elix, ramen, mon,stat1,stat2,stat3,stat4)
                    if skill[1] == 1:
                        if uy[4]>=100:
                            uy[3] -= skill[0]
                            uy[4]-=100
                        if uy[4]<1000:
                            print("마나부족! 아무것도 하지 못했다....")

                    elif skill[1] == 2:
                        if uy[4] >= 300:
                            uy[3] = skill[0]
                            uy[4] -= 300
                        if uy[4] < 300:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[1] == 3:
                        if uy[4] >= 1000:
                            mon[2] = skill[0]
                            uy[4] -= 1000
                        if uy[4]<1000:
                            print("마나부족! 아무것도 하지 못했다....")

                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1

                if mon[2] <= 0:
                    mon[2] = 0
                    print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                    print("")

                    for i in range(1, 5):
                        x = random.randint(2, 6)
                        uy[i] += round((uy[i] * x / 100))
                        king[i] += round((king[i] * x / 100))
                        yak[i] += round((yak[i] * x / 100))
                        bow[i] += round((bow[i] * x / 100))

                        print(f"{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                        print(f"{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                        print(f"{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                        print(f"{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                        print("=" * 50)
                        if mon[0] == '디아복로👹' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[0] = 1
                        elif mon[0] =='우연🤨' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[1] = 1
                        elif mon[0] == '일성킴👺' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[2] = 1
                        elif mon[0] == '민주석😏' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[3] = 1
                        elif mon[0] == '규범👽' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[4] = 1
                        elif mon[0] == '철몸😾' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[5] = 1
                        elif mon[0] == '아르헨도⚽' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[6] = 1

                        if  Mon_Status.boss_kill_list[0] == 1 and  Mon_Status.boss_kill_list[1] == 1 and  Mon_Status.boss_kill_list[2] == 1 and \
                                Mon_Status.boss_kill_list[3] == 1 and  Mon_Status.boss_kill_list[4] == 1 and  Mon_Status.boss_kill_list[5] == 1 and \
                                Mon_Status.boss_kill_list[6] == 1:
                            print("의용군 파티가 다시 한번 세상을 구했습니다!\n 중간계에 평화가 찾아왔습니다.")
                            exit()

                        return 1,potion,elix,ramen

                elif select == 3:
                    print(f"{uy[0]}이 도망을 선택했습니다.")
                    escape = random.randrange(1, 101)
                    if escape <= 10:
                         print("도망가는데 성공했습니다.")
                         return 0,potion,elix,ramen
                    else:
                        print("도망가는데 실패했습니다.")

                elif select == 4:
                    while (1):  # 예외처리시 헛턴낭비 방지 와일문
                        print("1.포션 2.엘릭서 3.라면")
                        select2 = int(input())
                        if select2 == 1:
                            potion -= 1
                            k = random.randrange(30, 81)
                            k1 = uy[3] * k // 100
                            uy[3] = uy[3] + k1
                            uy[4] = uy[4] + k1
                            print(f"체,마력이 {k1}만큼 올랐습니다.")
                            break
                        elif select2 == 2 and elix>=1:
                            print("🍷\033[35m엘릭서 사용\033[0;38m🍷")
                            elix_status += 10
                            elix -= 1
                            break
                        elif select2 == 3 and ramenturn == 0:
                            if ramen >= 1:
                                print("라면!")
                                ramen -= 1
                                ramenturn += 2
                                break
                            if ramen == 0:
                                print("라면없음")
                        elif select2 == 3 and ramenturn >= 1:
                            print("이미 끓이는중 입니다")

                        else:
                            print("잘못된 입력입니다.")
        if king[3] <= 0:
            pass
        elif king[3] >= 0:
                playercheck = 2
                printstat(mon, uy, king, yak, bow, potion, elix, ramen)
                print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
                select = int(input())
                if select == 1:
                    print(f"{king[0]}가 {mon[0]}(를)을 공격했습니다.")
                    print("")
                    if mon[2] >= 0:
                            atk_king = random.randint(king[1], king[2] + 1)
                            print(f"{mon[0]}의 체력이 {atk_king}만큼 줄었습니다.")
                            mon[2] -= atk_king
                            print("")
                            print(f"현재 몬스터 체력:{mon[2]}")

                elif select == 2:
                    skill = skillcheck(playercheck, win, potion, elix, ramen, mon, stat1, stat2, stat3, stat4)
                    if skill[1] == 1:
                        if king[4]>=100:
                            mon[2] -= skill[0]
                            king[4] -= 100
                        if king[4]<100:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[1] == 2:
                        if king[4] >= 300:
                            king[3] = skill[0]
                            king[4] -= 300
                        if king[4] < 300:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[4] == 3:
                        if king[4] >= 1000:
                            uy[3] += skill[0]
                            king[3] += skill[1]
                            yak[3] += skill[2]
                            bow[3] += skill[3]
                            king[4] -= 1000
                        if king[4] <1000:
                            print("마나부족! 아무것도 하지 못했다....")
                        if mon[2] <= 0:
                            print("=" * 50)
                            print("의용군 파티의 승리입니다!")
                            win += 1

                if mon[2] <= 0:
                        mon[2] = 0
                        print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                        print("")

                        for i in range(1, 5):
                            x = random.randint(2, 6)
                            uy[i] += round((uy[i] * x / 100))
                            king[i] += round((king[i] * x / 100))
                            yak[i] += round((yak[i] * x / 100))
                            bow[i] += round((bow[i] * x / 100))

                            print(f"{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                            print(f"{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                            print(f"{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                            print(f"{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                            print("=" * 50)

                            if mon[0] == '디아복로👹' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[0] = 1
                            elif mon[0] == '우연🤨' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[1] = 1
                            elif mon[0] == '일성킴👺' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[2] = 1
                            elif mon[0] == '민주석😏' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[3] = 1
                            elif mon[0] == '규범👽' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[4] = 1
                            elif mon[0] == '철몸😾' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[5] = 1
                            elif mon[0] == '아르헨도⚽' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[6] = 1

                            if Mon_Status.boss_kill_list[0] == 1 and Mon_Status.boss_kill_list[1] == 1 and \
                                    Mon_Status.boss_kill_list[2] == 1 and \
                                    Mon_Status.boss_kill_list[3] == 1 and Mon_Status.boss_kill_list[4] == 1 and \
                                    Mon_Status.boss_kill_list[5] == 1 and \
                                    Mon_Status.boss_kill_list[6] == 1:
                                print("의용군 파티가 다시 한번 세상을 구했습니다!\n 중간계에 평화가 찾아왔습니다.")
                                exit()

                        return 1, potion, elix,ramen

                elif select == 3:
                    print(f"{king[0]}가 도망을 선택했습니다.")
                    escape = random.randrange(1, 101)
                    if escape <= 10:
                        print("도망가는데 성공했습니다.")
                        return 0,potion,elix,ramen
                    else:
                        print("도망가는데 실패했습니다.")

                elif select == 4:
                    while (1):  # 예외처리시 헛턴낭비 방지 와일문
                        print("1.포션 2.엘릭서 3.라면")
                        select2 = int(input())
                        if select2 == 1:
                            potion -= 1
                            u = random.randrange(30, 81)
                            u1 = king[3] * u // 100
                            king[3] += u1
                            king[4] += u1
                            print(f"체,마력이 {u1}만큼 올랐습니다.")
                            break

                        elif select2 == 2 and elix>=1:
                            print("🍷\033[35m엘릭서 사용\033[0;38m🍷")
                            elix_status += 10
                            elix -= 1
                            break

                        elif select2 == 3 and ramenturn == 0:
                            if ramen >= 1:
                                print("라면!")
                                ramen -= 1
                                ramenturn += 2
                                break
                            if ramen == 0:
                                print("라면없음")
                        elif select2 == 3 and ramenturn >= 1:
                            print("이미 끓이는중 입니다")

                        else:
                            print("잘못된 입력입니다.")

        if yak[3] <= 0:
            pass
        elif yak[3] >= 0:
                playercheck = 3
                printstat(mon, uy, king, yak, bow, potion, elix, ramen)
                print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
                select = int(input())
                if select == 1:
                    print(f"{yak[0]}가 {mon[0]}(를)을 공격했습니다.")
                    if mon[2] >= 0:
                            atk_yak = random.randint(king[1], king[2] + 1)
                            print(f"{mon[0]}의 체력이 {atk_yak}만큼 줄었습니다.")
                            mon[2] -= atk_yak
                            print("")
                            print(f"현재 몬스터 체력:{mon[2]}")
                    print("")

                elif select == 2:
                    skill = skillcheck(playercheck, win, potion, elix, ramen, mon, stat1, stat2, stat3, stat4)
                    if skill[1] == 1:
                        if yak[4] >= 100:
                            mon[2] -= skill[0]
                            yak[4] -= 100
                        if yak[4] < 100:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[1] == 2:
                        if yak[4] >= 300:
                            yak[3] = skill[0]
                            yak[4] -= 300
                        if yak[4] < 300:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[1] == 3:
                        ramen += skill[0]

                if mon[2] <= 0:
                    print("=" * 50)
                    print("의용군 파티의 승리입니다!")
                    win += 1

                if mon[2] <= 0:
                    mon[2] = 0
                    print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                    print("")

                    for i in range(1, 5):
                        x = random.randint(2, 6)
                        uy[i] += round((uy[i] * x / 100))
                        king[i] += round((king[i] * x / 100))
                        yak[i] += round((yak[i] * x / 100))
                        bow[i] += round((bow[i] * x / 100))

                        print(f"{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                        print(f"{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                        print(f"{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                        print(f"{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                        print("=" * 50)

                        if mon[0] == '디아복로👹' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[0] = 1
                        elif mon[0] == '우연🤨' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[1] = 1
                        elif mon[0] == '일성킴👺' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[2] = 1
                        elif mon[0] == '민주석😏' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[3] = 1
                        elif mon[0] == '규범👽' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[4] = 1
                        elif mon[0] == '철몸😾' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[5] = 1
                        elif mon[0] == '아르헨도⚽' and mon[2] <= 0:
                            Mon_Status.boss_kill_list[6] = 1

                        if Mon_Status.boss_kill_list[0] == 1 and Mon_Status.boss_kill_list[1] == 1 and \
                                Mon_Status.boss_kill_list[2] == 1 and \
                                Mon_Status.boss_kill_list[3] == 1 and Mon_Status.boss_kill_list[4] == 1 and \
                                Mon_Status.boss_kill_list[5] == 1 and \
                                Mon_Status.boss_kill_list[6] == 1:
                            print("의용군 파티가 다시 한번 세상을 구했습니다!\n 중간계에 평화가 찾아왔습니다.")
                            exit()
                        return 1,potion,elix,ramen

                elif select == 3:
                    print(f"{yak[0]}이 도망을 선택했습니다.")
                    escape = random.randrange(1, 101)
                    if escape <= 10:
                        print("도망가는데 성공했습니다.")
                        return 0,potion,elix,ramen
                    else:
                        print("도망가는데 실패했습니다.")

                elif select == 4:
                    while (1):  # 예외처리시 헛턴낭비 방지 와일문
                        print("1.포션 2.엘릭서 3.라면")
                        select2 = int(input())
                        if select2 == 1:
                            potion -= 1
                            h = random.randrange(30, 81)
                            h1 = yak[3] * h // 100
                            yak[3] += h1
                            yak[4] += h1
                            print(f"체,마력이 {h1}만큼 올랐습니다.")
                            break

                        elif select2 == 2 and elix>=1:
                            print("🍷\033[35m엘릭서 사용\033[0;38m🍷")
                            elix_status += 10
                            elix -= 1
                            break
                        elif select2 == 3 and ramenturn == 0:
                            if ramen >= 1:
                                print("라면!")
                                ramen -= 1
                                ramenturn += 2
                                break
                            if ramen == 0:
                                print("라면없음")
                        elif select2 == 3 and ramenturn >= 1:
                            print("이미 끓이는중 입니다")

                        else:
                            print("잘못된 입력입니다.")

        if bow[3] <= 0:
            pass
        elif bow[3] >= 0:
                playercheck = 4
                printstat(mon, uy, king, yak, bow, potion, elix, ramen)
                print("1.공격 2.스킬 3.도망 4.물약 / 넷 중 하나를 선택하십시오")
                select = int(input())
                if select == 1:
                    print(f"{bow[0]}가 {mon[0]}(를)을 공격했습니다.")
                    print("")
                    if mon[2] >= 0:
                        atk_bow = random.randint(bow[1], bow[2] + 1)
                        print(f"{mon[0]}의 체력이 {atk_bow}만큼 줄었습니다.")
                        mon[2] -= atk_bow
                        print("")
                        print(f"현재 몬스터 체력:{mon[2]}")


                elif select == 2:
                    skill = skillcheck(playercheck, win, potion, elix, ramen, mon, stat1, stat2, stat3, stat4)
                    if skill[1] == 1:
                        if bow[4] >= 100:
                            mon[2] -= skill[0]
                            bow[4] -= 100
                        if bow[4] < 100:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[1] == 2:
                        if bow[4] >= 300:
                            bow[3] = skill[0]
                            bow[4] -= 300
                        if bow[4] < 300:
                            print("마나부족! 아무것도 하지 못했다....")
                    elif skill[2] == 3:
                        if bow[4] >= 1000:
                            print("남은체력: 보우연재%d,상대%d" % (skill[0], skill[1]))
                            bow[3] = skill[0]
                            mon[2] = skill[1]
                            bow[4] -= 1000
                        if bow[4] < 1000:
                            print("마나부족! 아무것도 하지 못했다....")
                    if mon[2] <= 0:
                        print("=" * 50)
                        print("의용군 파티의 승리입니다!")
                        win += 1

                if mon[2] <= 0:
                        mon[2] = 0
                        print(f"{mon[0]}의 체력이 {mon[2]}이 됐습니다.")
                        print("")

                        for i in range(1, 5):
                            x = random.randint(2, 6)
                            uy[i] += round((uy[i] * x / 100))
                            king[i] += round((king[i] * x / 100))
                            yak[i] += round((yak[i] * x / 100))
                            bow[i] += round((bow[i] * x / 100))

                            print(f"{uy[0]}의 최소 공격력:{uy[1]}\n{uy[0]}의 최대 공격력:{uy[2]}\n{uy[0]}의 체력:{uy[3]}\n{uy[0]}의 마력:{uy[4]}")
                            print(f"{king[0]}의 최소 공격력:{king[1]}\n{king[0]}의 최대 공격력:{king[2]}\n{king[0]}의 체력:{king[3]}\n{king[0]}의 마력:{king[4]}")
                            print(f"{yak[0]}의 최소 공격력:{yak[1]}\n{yak[0]}의 최대 공격력:{yak[2]}\n{yak[0]}의 체력:{yak[3]}\n{yak[0]}의 마력:{yak[4]}")
                            print(f"{bow[0]}의 최소 공격력:{bow[1]}\n{bow[0]}의 최대 공격력:{bow[2]}\n{bow[0]}의 체력:{bow[3]}\n{bow[0]}의 마력:{bow[4]}")
                            print("=" * 50)

                            if mon[0] == '디아복로👹' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[0] = 1
                            elif mon[0] == '우연🤨' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[1] = 1
                            elif mon[0] == '일성킴👺' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[2] = 1
                            elif mon[0] == '민주석😏' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[3] = 1
                            elif mon[0] == '규범👽' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[4] = 1
                            elif mon[0] == '철몸😾' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[5] = 1
                            elif mon[0] == '아르헨도⚽' and mon[2] <= 0:
                                Mon_Status.boss_kill_list[6] = 1

                            if Mon_Status.boss_kill_list[0] == 1 and Mon_Status.boss_kill_list[1] == 1 and \
                                    Mon_Status.boss_kill_list[2] == 1 and \
                                    Mon_Status.boss_kill_list[3] == 1 and Mon_Status.boss_kill_list[4] == 1 and \
                                    Mon_Status.boss_kill_list[5] == 1 and \
                                    Mon_Status.boss_kill_list[6] == 1:
                                print("의용군 파티가 다시 한번 세상을 구했습니다!\n 중간계에 평화가 찾아왔습니다.")
                                exit()
                            # 부두목 6인과 디아복로까지 죽였을때 엔딩 여기 넣어야 됨
                        return 1,potion,elix,ramen

                elif select == 3:
                    print(f"{bow[0]}이 도망을 선택했습니다.")
                    escape = random.randrange(1, 101)
                    if escape <= 10:
                        print("도망가는데 성공했습니다.")
                        return 0,potion,elix,ramen
                    else:
                        print("도망가는데 실패했습니다.")

                elif select == 4:
                    while (1):  # 예외처리시 헛턴낭비 방지 와일문
                        print("1.포션 2.엘릭서 3.라면")
                        select2 = int(input())
                        if select2 == 1:
                            potion -= 1
                            l = random.randrange(30, 81)
                            l1 = bow[3] * l // 100
                            bow[3] += l1
                            bow[4] += l1
                            print(f"체,마력이 {l1}만큼 올랐습니다.")
                            break

                        elif select2 == 2 and elix>=1:
                            print("🍷\033[35m엘릭서 사용\033[0;38m🍷")
                            elix_status += 10
                            elix -= 1
                            break

                        elif select2 == 3 and ramenturn == 0:
                            if ramen >= 1:
                                print("라면!")
                                ramen -= 1
                                ramenturn += 2
                                break
                            if ramen == 0:
                                print("라면없음")
                        elif select2 == 3 and ramenturn >= 1:
                            print("이미 끓이는중 입니다")

                        else:
                            print("잘못된 입력입니다.")

                if ramenturn >= 1:
                    ramenturn -= 1
                    print("라면끓이는중")
                    if ramenturn == 0:
                        print("라면완성! 초코의용군 hp,mp50%회복")
                        print("라면완성! 킹기태 hp50%회복")
                        print("라면완성! 약범규 hp50%회복")
                        print("라면완성! 보우연재 hp50%회복")
                        if uy[2] + hpmax1 / 2 <= hpmax1:
                            uy[2] += hpmax1 / 2
                        else:
                            uy[2] = hpmax1

                        if king[2] + hpmax2 / 2 <= hpmax2:
                            king[2] += hpmax2 / 2
                        else:
                            king[2] = hpmax2

                        if yak[2] + hpmax3 / 2 <= hpmax3:
                            yak[2] += hpmax3 / 2
                        else:
                            yak[2] = hpmax3

                        if bow[2] + hpmax4 / 2 <= hpmax4:
                            bow[2] += hpmax4 / 2
                        else:
                            bow[2] += hpmax4

                        if uy[3] + mpmax1 / 2 <= mpmax1:
                            uy[3] += mpmax1 / 2
                        else:
                            uy[3] = mpmax1
                        if uy[3] + hpmax2 / 2 <= hpmax2:
                            king[3] += mpmax2 / 2
                        else:
                            king[3] = mpmax2
                        if yak[3] + hpmax3 / 2 <= hpmax3:
                            yak[3] += mpmax3 / 2
                        else:
                            yak[3] = mpmax3
                        if uy[3] + hpmax4 / 2 <= hpmax4:
                            bow[3] += mpmax4 / 2
                        else:
                            bow[3] = mpmax4
                if elix_status ==0:
                    m = random.randrange(0, 4)
                    if players[m][5] == True:
                        pass
                    elif players[m][3] >= 0:
                        print(f"{mon[0]}이 {players[m][0]}(을)를 때렸습니다.")
                        players[m][3] -= mon[1]
                        print(f"{players[m][0]}의 체력이 {mon[1]}만큼 줄었습니다.")
                        print(f"{players[m][0]}의 현재 체력:{players[m][3]}")
                        if players[m][3] <= 0:

                            print(f"{players[m][0]}(이)가 기절했습니다. 아웃.")
                            players[m][5] = True
                            if players[m][5] == True:
                                    players[m][1] = 0
                                    players[m][2] = 0
                                    players[m][3] = 0
                                    players[m][4] = 0
                elif elix_status >= 1:  # 엘릭서 턴 존재시 몹공격x 구문출력
                    print("👾\033[0;30m몹의 공격\033[0;38m")
                    print(
                        "🛡\033[31m엘\033[0;37m\033[32m릭\033[0;37m\033[33m서\033[0;37m \033[34m무\033[0;37m\033[35m적\033[0;38m!🛡")
                    elix_status -= 1

        if uy[3] == 0 and king[3] == 0 and yak[3] == 0 and bow[3] == 0:
            print("=" * 50)
            print("👹의용군 파티는 전멸했습니다.\n디아복로가 중간계를 지배합니다...👹")
            exit()


def map():                                                              #맵총괄함수

    col=0
    row=0
    step=0
    colrow = []
    floor = 1
    floorcnt=1
    battlecnt=0
    win=1
    portcol=portrow=0
    potion = 3
    elix =1
    ramen = 5
    stat1 = [0, 0, 0, 0]
    stat2 = [0, 0, 0, 0]
    stat3 = [0, 0, 0, 0]
    stat4 = [0, 0, 0, 0]
    while (1):
        dummy = mapinfo()                                               #클래스 사용을 위해 더미변수에 담음
        map = dummy.maping()
        potionrand=dummy.rand2()                                        #rand2클래스에서 랜덤값 받아옴
        a = party(potion,elix, ramen, stat1,stat2,stat3,stat4)
        b = a.party1()
        c = a.party2()
        d = a.party3()
        e = a.party4()
        print("소지 포션,엘릭서,라면",a.inven())
        for j in range (0,16):                                          #오류있어서 안보이는 16번째줄 배열만듬
            map[j][15]=99

        if potionrand<=4:
            print("이동중 포션 드랍")

        if(step%3==0):                                 #몬스터 갱신
            print("갱신")
            colrow = []
            for i in range(0,21):
                randcol,randrow=dummy.rand()
                colrow.append(randcol)
                colrow.append(randrow)

        for i in range (0,39,2):
            map[colrow[i]][colrow[i+1]] = 10                            #몬스터 위장
        if floor<5:
            if battlecnt/10==1 or step==0:
                portcol,portrow=dummy.rand()
                battlecnt=0
            map[portcol][portrow] = 11                        #포탈 위장

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
            sign,potion,elix, ramen=battle(win,potion,elix,ramen,stat1,stat2,stat3,stat4)
            if sign==1:
                if random.randrange(0,2)==0:
                    for i in range (0,4):
                        print(stat1[i],stat2[i],"!!!!!!!!!!")
                        stat1[i] += round(b[i + 1]*(random.randrange(2,6)/100))
                        stat2[i] += round(c[i + 1] * (random.randrange(2, 6) / 100))
                        stat3[i] += round(d[i + 1] * (random.randrange(2, 6) / 100))
                        stat4[i] += round(e[i + 1] * (random.randrange(2, 6) / 100))
                    party(potion, elix, ramen, stat1,stat2,stat3,stat4)
                    if random.randrange(1,1001)<=5:
                        print("엘릭서드랍")
                        elix+=1
                    else:
                        print("포션드랍")
                        potion+=1
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
