import Agent
from collections import deque
import random

def SUBTEAM_2_PLACEHOLDER(groups,agents,aChance):
    subteam_2_output = [random.random() <= aChance and a.phase != 'symptomatic' for a in agents]
    q = deque(subteam_2_output)
    for g in groups: g.willGoOut = [q.popleft() for _ in g]

class Groups:
    class Group:
        def __init__(self,sz):
            self.agents = [Agent.Agent(super.disease) for _ in range(sz)]
            self.preference = -1
            self.willGoOut = [False]*len(self.agents)

        def setPreference(self): #KPR HERE
            self.preference = random.randint(0,super.numRestaurants-1)

        def getAttendees(self): #GROUP DECISION HERE
            if random.random() <= super.gChance:
                return [a for i,a in enumerate(self.agents) if self.willGoOut[i]]
            else:
                return []

        def __len__(self): return len(self.agents)
        def __getitem__(self, i): return self.agents[i]
        def __setitem__(self,i,v): self.agents[i] = v
        def __delitem__(self,i): self.agents.pop(i)

    def __init__(self,numGroups,numAgents,numRestaurants,gChance,aChance,disease):
        assert numGroups <= numAgents
        self.numRestaurants = numRestaurants
        self.disease = disease
        self.gChance = gChance
        self.aChance = aChance

        groupSizes = [1]*numGroups
        for _ in range(numAgents-numGroups): groupSizes[random.randint(0,numGroups-1)] += 1
        self.groups = [self.Group(sz) for sz in groupSizes]
        self.agents = [a for g in self.groups for a in g]

    def getAttendees(self):
        def getPreferences():
            for g in self.groups: g.setPreference()
            return [g.preference for g in self.groups]
        def getGoingOut():
            SUBTEAM_2_PLACEHOLDER(self.groups,self.agents,self.aChance)
            return [g.getAttendees() for g in self.groups]
        prefs, out = getPreferences(), getGoingOut()
        attendees = [[] for _ in range(self.numRestaurants)]
        for p,g in zip(prefs,out):
            attendees[p].append(g)
        return attendees
    
    def passDay(self):
        attendance = self.getAttendees()
        self.disease.infect(attendance)
        for a in self.agents: a.passDay(self.disease)
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

    def __len__(self): return len(self.groups)
    def __getitem__(self, i): return self.groups[i]
    def __setitem__(self,i,v): self.groups[i] = v
    def __delitem__(self,i): self.groups.pop(i)
