import Agent
import random

gChance = 0.05
aChance = 0.9

def initPopulations(numGroups,numAgents,numRestaurants):
    groupSizes = [1]*numGroups
    for _ in range(numAgents-numGroups): 
        groupSizes[random.randint(0,numGroups-1)] += 1
    return [set(Agent.Agent() for _ in range(sz)) for sz in groupSizes]
    
def getPreferences(groups,numRestaurants):
    return [random.randint(0,numRestaurants-1) for _ in groups]

def getGoingOut(groups):
    outs = [set()]*len(groups)
    for i,g in enumerate(groups):
        if random.random() <= gChance:
            outs[i] = set(a for a in g if a.willGoOut(aChance))
    return outs

def getAttendees(prefs,out,numRestaurants):
    attendees = [[] for _ in range(numRestaurants)]
    for p,g in zip(prefs,out):
        attendees[p].extend([a for a in g])
    return attendees

def passDay(groups):
    for g in groups:
        for a in g:
            a.passDay()