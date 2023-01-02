import random



class Mon_Status:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp


def Mobs():
    Diablo = Mon_Status["디아블로", random.randint(2500, 8001), random.randint(10000, 20001) ]
    Wuyeon = Mon_Status["우연", random.randint(1000, 3001), random.randint(5000, 10001)]
    Ilsungkim = Mon_Status["일성킴", random.randint(1000, 3001), random.randint(5000, 10001)]
    MinJuSeok = Mon_Status["민주석", random.randint(1000, 3001), random.randint(5000, 10001)]
    KyuBeom = Mon_Status["규범", random.randint(1000, 3001), random.randint(5000, 10001)]
    ChulMoom = Mon_Status["철몸", random.randint(1000, 3001), random.randint(5000, 10001)]
    Ado = Mon_Status["아르헨도", random.randint(1000, 3001), random.randint(5000, 10001)]
    BugBear = Mon_Status["버그베어", 350, random.randint(550, 901)]
    Skull = Mon_Status["해골", 220, random.randint(480, 801)]
    gull = Mon_Status["구울", 180, random.randint(450, 701)]
    Zombie = Mon_Status["좀비", 100, random.randint(300, 501)]

























def Mon_Per():
    a = random.randrange(1, 1001)
    number = a
    MON=Mon_Status()
    if number <= 2:
        return MON.Diablo()
    elif 3 <= number <= 12:
        return MON.Wuyeon()
    elif 13 <= number <= 22:
        return MON.IlsungKim()
    elif 23 <= number <= 32:
        return MON.MinJuSeok()
    elif 33 <= number <= 42:
        return MON.KyuBeom()
    elif 43 <= number <= 52:
        return MON.ChulMoom()
    elif 53 <= number <= 62:
        return MON.Ado()
    elif 63 <= number <= 102:
        return MON.BugBear()
    elif 103 <= number <= 122:
        return MON.Skull()
    elif 123 <= number <= 422:
        return MON.Gull()
    else:
        return MON.Zombie()




def battle(win):
