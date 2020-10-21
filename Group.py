import Agent
from collections import deque
import random

def SUBTEAM_2_PLACEHOLDER(agents,aChance):
    return [random.random() <= aChance and a.phase != 'symptomatic' for a in agents]

class Groups:
    def __init__(self,numGroups,numAgents,numRestaurants,gChance,aChance,disease):
        assert numGroups <= numAgents
        groupSizes = [1]*numGroups
        for _ in range(numAgents-numGroups): 
            groupSizes[random.randint(0,numGroups-1)] += 1
        self.groups = [[Agent.Agent(disease) for _ in range(sz)] for sz in groupSizes]
        self.agents = [a for g in self.groups for a in g]
        self.numRestaurants = numRestaurants
        self.disease = disease
        self.gChance = gChance
        self.aChance = aChance

    def getAttendees(self):
        def getPreferences(): #KPR HERE
            return [random.randint(0,self.numRestaurants-1) for _ in self.groups]
        def getGoingOut(): #GROUP DECISION HERE
            willGoOut = deque(SUBTEAM_2_PLACEHOLDER(self.agents,self.aChance))
            outs = [[]]*len(self.groups)
            for i,g in enumerate(self.groups):
                if random.random() <= self.gChance:
                    outs[i] = [a for a in g if willGoOut.popleft()]
            return outs
        prefs, out = getPreferences(), getGoingOut()
        attendees = [[] for _ in range(self.numRestaurants)]
        for p,g in zip(prefs,out):
            attendees[p].append(g)
        return attendees
    
    def passDay(self):
        attendance = self.getAttendees()
        self.disease.infect(attendance)
        for g in self.groups:
            for a in g:
                a.passDay(self.disease)
        return attendance

    def getWinners(self,attendance):
        attendance = set(a for g in attendance for a in g)
        attendeesWin = len(attendance) <= len(self.agents)/2
        homiesWin = len(attendance) > len(self.agents)/2
        winners = []
        for a in self.agents:
            if a in attendance: winners.append(attendeesWin and a.isHealthy())
            else: winners.append(homiesWin or a.isSick())
        return winners
                
    def getSick(self):
        return sum(1 for g in self.groups for a in g if a.isSick())
    
    def getHealthy(self):
        return sum(1 for g in self.groups for a in g if a.isHealthy())

    def __len__(self):
        return len(self.groups)
    
    def __getitem__(self, i):
        return self.groups[i]
    
    def __setitem__(self,i,v):
        self.groups[i] = v
        
    def __delitem__(self,i):
        self.groups.pop(i)
