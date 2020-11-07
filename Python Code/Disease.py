import PythonC.DiseaseC as dc
import random

class Disease:
    def __init__(self,startSickChance,startSymptomaticChance,rateOfSpread,
                 sickTime,incubationTime,immuneTime):
        self.startSickChance = startSickChance
        self.startSymptomaticChance = startSymptomaticChance
        self.rateOfSpread = rateOfSpread
        self.sickTime = sickTime
        self.incubationTime = incubationTime
        self.immuneTime = immuneTime

    def infect(self,attendance):
        for restaurant in attendance:
            numInfected = sum(1 for g in restaurant for a in g if a.isSick())
            chanceOfInfection = dc.getChanceOfInfection(self.rateOfSpread,numInfected)
            for g in restaurant: 
                for a in g:
                    if random.random() <= chanceOfInfection:
                        a.infect(self)
            