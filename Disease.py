import math
import random

forceSick = 5
startSickChance = 0.01
startSickSymptomaticChance = 0.5
rateOfSpread = 0.05
sickTime = 3
incubationTime = 14
immuneTime = 90
chanceOfDeath = 0.02

def squash(x):
  return 2/(1+math.exp(-x)) - 1

def infect(attendees):
    for restaurant in attendees:
        numInfected = sum(1 for a in restaurant if a.isSick())
        chanceOfInfection = 1-((1-rateOfSpread)**numInfected)
        for a in restaurant:
            if random.random() <= chanceOfInfection:
                a.infect()
            