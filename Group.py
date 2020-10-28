import GroupC as gc
import Agent
import Brain
from collections import deque
import random

MAX_GROUP_SIZE = 10

def SUBTEAM_2_PLACEHOLDER(groups,agents,aChance):
    subteam_2_output = [random.random() <= aChance and a.phase != 'symptomatic' for a in agents]
    q = deque(subteam_2_output)
    for g in groups: g.willGoOut = [a.setwillGoOut(q.popleft()) for a in g]

class Groups:
    class Group:
        def __init__(self,sz,disease):
            self.agents = [Agent.Agent(disease) for _ in range(sz)]
            self.brain = Brain.Brain([2*sz,2])
            self.score = 0
            self.preference = -1
            self.willGoOut = [False]*len(self.agents)
            self.wonLastRound = [True]*len(self.agents)
            self.goingOut = False

        def setPreference(self,numRestaurants): #KPR HERE
            self.preference = random.randint(0,numRestaurants-1)

        def getAttendees(self): #GROUP DECISION HERE
            def groupGoingOut():
                brainOutput = self.brain.computeOutput(self.willGoOut+self.wonLastRound)
                self.goingOut = brainOutput[0] > brainOutput[1]
                return self.goingOut
            return [a for a in self.agents if a.willGoOut] if groupGoingOut() else []

        def updateGroup(self):
            self.wonLastRound = [a.wonLastRound for a in self.agents]
            dayScore = sum(1 if a.wonLastRound else -1 for a in self.agents)
            self.score += dayScore
            if dayScore < 0:
                self.brain.backprop([not self.goingOut, self.goingOut],1)
                self.brain.applyGradient()

        def __len__(self): return len(self.agents)
        def __getitem__(self, i): return self.agents[i]
        def __setitem__(self,i,v): self.agents[i] = v
        def __delitem__(self,i): self.agents.pop(i)

    def __init__(self,numGroups,numAgents,numRestaurants,gChance,aChance,disease):
        assert numGroups*MAX_GROUP_SIZE >= numAgents
        self.numRestaurants = numRestaurants
        self.disease = disease
        self.gChance = gChance
        self.aChance = aChance

        groupSizes = gc.getGroupSizes(numAgents,numGroups,MAX_GROUP_SIZE)
        self.groups = [self.Group(sz,disease) for sz in groupSizes]
        self.agents = [a for g in self.groups for a in g]

    def getAttendees(self):
        def getPreferences():
            for g in self.groups: g.setPreference(self.numRestaurants)
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

    def getWinners(self):
        sickness = [a.isSick() for a in self.agents]
        winners = gc.getWinners(self.agents,sickness)
        for g in self.groups:
            g.updateGroup()
        return winners

    def getScores(self):
        return sorted(g.score for g in self.groups)
                
    def getSick(self):
        return sum(1 for g in self.groups for a in g if a.isSick())
    
    def getHealthy(self):
        return sum(1 for g in self.groups for a in g if a.isHealthy())

    def __len__(self): return len(self.groups)
    def __getitem__(self, i): return self.groups[i]
    def __setitem__(self,i,v): self.groups[i] = v
    def __delitem__(self,i): self.groups.pop(i)
