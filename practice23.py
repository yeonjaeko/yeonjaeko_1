import random



class Mon_Status:
    def Diablo(self):
        self.name = '디아복로'
        self.attack = random.randrange(2500, 8001)
        self.hp = random.randrange(10000, 20001)
        return [self.name, self.attack, self.hp]

    def Wuyeon(self):
        self.name = '우연'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def Ilsungkim(self):
        self.name = '일성킴'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def MinJuSeok(self):
        self.name = '민주석'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def KyuBeom(self):
        self.name = '규범'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def ChulMoon(self):
        self.name = '철몸'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]

    def Ado(self):
        self.name = '아르헨도'
        self.attack = random.randrange(1000, 3001)
        self.hp = random.randrange(5000, 10001)
        return [self.name, self.attack, self.hp]


    def BugBear(self):
        self.name = '버그베어'
        self.attack = random.randrange(350, 351)
        self.hp = random.randrange(550, 901)
        return [self.name, self.attack, self.hp]

    def Skull(self):
        self.name = '해골'
        self.attack = random.randrange(220, 221)
        self.hp = random.randrange(480, 801)
        return [self.name, self.attack, self.hp]

    def Gull(self):
        self.name = '구울'
        self.attack = random.randrange(180, 181)
        self.hp = random.randrange(450, 701)
        return [self.name, self.attack, self.hp]

    def Zombie(self):
        self.name = '좀비'
        self.attack = random.randrange(100, 101)
        self.hp = random.randrange(300, 501)
        return [self.name, self.attack, self.hp]







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


print(Mon_Per())

