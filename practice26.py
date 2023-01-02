import random


class party:
    def __init__(self,win,potion,elix):
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
        self.attack1 = round(random.randrange(101, 151) * ((self.win * self.rand / 100) + 1))
        self.hp1 = round(500 * ((self.win * self.rand / 100) + 1))
        self.mp1 = round(300 * ((self.win * self.rand / 100) + 1))
        return ["의용군", self.attack1, self.hp1, self.mp1]

    def party3(self):
        self.attack3 = round(random.randrange(101, 151) * ((self.win * self.rand / 100) + 1))
        self.hp3 = round(500 * ((self.win * self.rand / 100) + 1))
        self.mp3 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack3, self.hp3, self.mp3

    def party4(self):
        self.attack4 = round(random.randrange(101, 151) * ((self.win * self.rand / 100) + 1))
        self.hp4 = round(500 * ((self.win * self.rand / 100) + 1))
        self.mp4 = round(300 * ((self.win * self.rand / 100) + 1))
        return self.attack4, self.hp4, self.mp4

    def inven(self):
        return self.potion, self.elix
