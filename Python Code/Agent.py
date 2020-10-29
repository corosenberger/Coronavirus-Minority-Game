import random

IMMUNE = 0
HEALTHY = 1
ASYMPTOMATIC = 2
SYMPTOMATIC = 3
NUM_PHASES = 4

class Agent:
    def __init__(self,disease):
        self.wonLastRound = True
        self.willGoOut = False
        self.wentOut = False
        if random.random() <= disease.startSickChance:
            if random.random() <= disease.startSymptomaticChance:
                self.phase = SYMPTOMATIC
                self.daysLeft = random.randint(1,disease.sickTime+1)
            else:
                self.phase = ASYMPTOMATIC
                self.daysLeft = random.randint(1,disease.incubationTime+1)
        else:
            self.phase = HEALTHY
            self.daysLeft = -1
        self.passDay(disease)
        
    def passDay(self,disease):
        if self.daysLeft > 0:
            self.daysLeft -= 1
        while self.daysLeft == 0:
            self.phase = (self.phase+1) % NUM_PHASES
            self.daysLeft = disease.sickTime if self.phase == SYMPTOMATIC else \
                disease.immuneTime if self.phase == IMMUNE else -1
    
    def infect(self,disease):
        if self.phase == HEALTHY:
            self.phase = ASYMPTOMATIC
            self.daysLeft = disease.incubationTime
    
    def isHealthy(self):
        return self.phase == HEALTHY or self.phase == IMMUNE
    
    def isSick(self):
        return self.phase == SYMPTOMATIC or self.phase == ASYMPTOMATIC
        