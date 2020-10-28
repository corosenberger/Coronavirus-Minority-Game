import random

class Agent:
    def __init__(self,disease):
        self.wonLastRound = True
        self.willGoOut = False
        if random.random() <= disease.startSickChance:
            if random.random() <= disease.startSymptomaticChance:
                self.phase = 'symptomatic'
                self.daysLeft = random.randint(1,disease.sickTime)
            else:
                self.phase = 'asymptomatic'
                self.daysLeft = random.randint(1,disease.incubationTime)
        else:
            self.phase = 'healthy'
            self.daysLeft = -1
        
    def passDay(self,disease):
        if self.daysLeft > 0:
            self.daysLeft -= 1
        if self.daysLeft == 0:
            if self.phase == 'asymptomatic':
                self.phase = 'symptomatic'
                self.daysLeft = disease.sickTime
            elif self.phase == 'symptomatic':
                self.phase = 'immune'
                self.daysLeft = disease.immuneTime
            else:
                self.phase = 'healthy'
                self.daysLeft = -1

    def setwillGoOut(self,wgo):
        self.willGoOut = wgo
        return self.willGoOut
    
    def infect(self,disease):
        if self.phase == 'healthy':
            self.phase = 'asymptomatic'
            self.daysLeft = disease.incubationTime
    
    def isHealthy(self):
        return self.phase == 'healthy' or self.phase == 'immune'
    
    def isSick(self):
        return self.phase == 'symptomatic' or self.phase == 'asymptomatic'
        