import PythonC.GroupC as gc
import Agent
import Brain
import random

MAX_GROUP_SIZE = 10

class Groups:
    class Group:
        def __init__(self,sz,disease):
            self.agents = [Agent.Agent(disease) for _ in range(sz)]
            self.brain = Brain.Brain([2*sz,2])
            self.brainInput = []
            self.score = 0
            self.preference = -1
            self.goingOut = False

        def setPreference(self,numRestaurants): #KPR HERE
            self.preference = random.randint(0,numRestaurants-1)

        def getAttendees(self): #GROUP DECISION HERE
            def groupGoingOut():
                brainOutput = self.brain.computeOutput(self.brainInput)
                self.goingOut = brainOutput[0] > brainOutput[1]
                return self.goingOut
            if groupGoingOut():
                for a in self.agents: a.wentOut = a.willGoOut
                return [a for a in self.agents if a.willGoOut]
            else:
                return []

        def updateGroup(self):
            dayScore = sum(1 if a.wonLastRound else -1 for a in self.agents)
            self.score += dayScore
            if dayScore < 0:
                self.brain.backprop([not self.goingOut, self.goingOut],1)
                self.brain.applyGradient()

        def __len__(self): return len(self.agents)
        def __getitem__(self, i): return self.agents[i]
        def __setitem__(self,i,v): self.agents[i] = v
        def __delitem__(self,i): self.agents.pop(i)

    def __init__(self,numGroups,numAgents,numRestaurants,disease):
        self.numRestaurants = numRestaurants
        self.disease = disease

        groupSizes = gc.getGroupSizes(numAgents,numGroups,MAX_GROUP_SIZE)
        self.groups = [self.Group(sz,disease) for sz in groupSizes]
        self.agents = [a for g in self.groups for a in g]

    def getAttendees(self):
        def getPreferences():
            for g in self.groups: g.setPreference(self.numRestaurants)
            return [g.preference for g in self.groups]
        def getGoingOut():
            return [g.getAttendees() for g in self.groups]
        prefs, outs = getPreferences(), getGoingOut()

        attendees = gc.getAttendees(prefs,outs,self.numRestaurants)
        return attendees
    
    def passDay(self, subteam2input):
        gc.processSubTeam2Input(self.groups,subteam2input)
        attendance = self.getAttendees()
        self.disease.infect(attendance)
        for a in self.agents: a.passDay(self.disease)
        return attendance

    def getWinners(self):
        winners = gc.getWinners(self.agents)
        for g in self.groups: g.updateGroup()
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
