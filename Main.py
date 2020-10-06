import Disease
import Group
from matplotlib import pyplot as plt

def main(numDays,startSickChance,startSymptomaticChance,rateOfSpread,sickTime,incubationTime,
         immuneTime,chanceOfDeath,numGroups,numAgents,numRestaurants,gChance,aChance):
    disease = Disease.Disease(startSickChance,startSymptomaticChance,rateOfSpread,
                 sickTime,incubationTime,immuneTime,chanceOfDeath)
    groups = Group.Groups(numGroups,numAgents,numRestaurants,gChance,aChance,disease)
    sick, healthy, dead = {}, {}, {}
    
    for i in range(numDays):
        sick[i] = groups.getSick()
        healthy[i] = groups.getHealthy()
        dead[i] = groups.getDead()
        groups.passDay()
        
    x = list(sick.keys())
    y = list((a,b,c) for a,b,c in zip(sick.values(),healthy.values(),dead.values()))
    plt.plot(x,y)

if __name__ == '__main__':
    #Disease inputs
    startSickChance=0.01
    startSymptomaticChance=0.5
    rateOfSpread=0.01
    sickTime=7
    incubationTime=14
    immuneTime=90
    chanceOfDeath=0.02
    
    #Groups inputs
    numGroups=2000
    numAgents=10000
    numRestaurants=10
    gChance=0.1
    aChance=1
    
    numDays=1000
         
    main(numDays,startSickChance,startSymptomaticChance,rateOfSpread,sickTime,incubationTime,
         immuneTime,chanceOfDeath,numGroups,numAgents,numRestaurants,gChance,aChance)