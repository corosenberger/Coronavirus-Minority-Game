import random

class Disease:
    def __init__(self,startSickChance,startSymptomaticChance,rateOfSpread,
                 sickTime,incubationTime,immuneTime,chanceOfDeath):
        self.startSickChance = startSickChance
        self.startSymptomaticChance = startSymptomaticChance
        self.rateOfSpread = rateOfSpread
        self.sickTime = sickTime
        self.incubationTime = incubationTime
        self.immuneTime = immuneTime
        self.chanceOfDeath = chanceOfDeath

    def infect(self,attendance):
        for restaurant in attendance:
            numInfected = sum(1 for a in restaurant if a.isSick())
            chanceOfInfection = 1-((1-self.rateOfSpread)**numInfected)
            for a in restaurant:
                if random.random() <= chanceOfInfection:
                    a.infect(self)
            