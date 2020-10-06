import random

class Agent:
    def __init__(self,disease):
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
                if random.random() <= disease.chanceOfDeath:
                    self.phase = 'dead'
                    self.daysLeft = -1
                else:
                    self.phase = 'immune'
                    self.daysLeft = disease.immuneTime
            else:
                self.phase = 'healthy'
                self.daysLeft = -1
    
    def infect(self,disease):
        if self.phase == 'healthy':
            self.phase = 'asymptomatic'
            self.daysLeft = disease.incubationTime
            
    def willGoOut(self,aChance):
        return random.random() <= aChance and self.phase != 'symptomatic' and self.phase != 'dead'
    
    def isHealthy(self):
        return self.phase == 'healthy' or self.phase == 'immune'
    
    def isSick(self):
        return self.phase == 'symptomatic' or self.phase == 'asymptomatic'
    
    def isDead(self):
        return self.phase == 'dead'
        