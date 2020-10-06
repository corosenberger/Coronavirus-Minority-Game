import Disease
import random

class Agent:
    def __init__(self,phase=None,daysLeft=-1):
        if phase is not None:
            self.phase = phase
            self.daysLeft = daysLeft
        elif random.random() <= Disease.startSickChance:
            if random.random() <= Disease.startSickSymptomaticChance:
                self.phase = 'symptomatic'
                self.daysLeft = random.randint(1,Disease.sickTime)
            else:
                self.phase = 'asymptomatic'
                self.daysLeft = random.randint(1,Disease.incubationTime)
        else:
            self.phase = 'healthy'
            self.daysLeft = -1
        
    def passDay(self):
        if self.daysLeft > 0:
            self.daysLeft -= 1
        if self.daysLeft == 0:
            if self.phase == 'asymptomatic':
                self.phase = 'symptomatic'
                self.daysLeft = Disease.sickTime
            elif self.phase == 'symptomatic':
                if random.random() <= Disease.chanceOfDeath:
                    self.phase = 'dead'
                    self.daysLeft = -1
                else:
                    self.phase = 'immune'
                    self.daysLeft = Disease.immuneTime
            else:
                self.phase = 'healthy'
                self.daysLeft = -1
    
    def infect(self):
        if self.phase == 'healthy':
            self.phase = 'asymptomatic'
            self.daysLeft = Disease.incubationTime
            
    def willGoOut(self,aChance):
        return random.random() <= aChance and self.phase != 'symptomatic' and self.phase != 'dead'
    
    def isHealthy(self):
        return self.phase == 'healthy' or self.phase == 'immune'
    
    def isSick(self):
        return self.phase == 'symptomatic' or self.phase == 'asymptomatic'
    
    def isDead(self):
        return self.phase == 'dead'
        