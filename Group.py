import Agent
import random

class Groups:
    def __init__(self,numGroups,numAgents,numRestaurants,gChance,aChance,disease):
        assert numGroups <= numAgents
        groupSizes = [1]*numGroups
        for _ in range(numAgents-numGroups): 
            groupSizes[random.randint(0,numGroups-1)] += 1
        self.groups = [set(Agent.Agent(disease) for _ in range(sz)) for sz in groupSizes]
        self.numRestaurants = numRestaurants
        self.disease = disease
        self.gChance = gChance
        self.aChance = aChance
    
    def passDay(self):
        def getAttendees():
            def getPreferences():
                return [random.randint(0,self.numRestaurants-1) for _ in self.groups]
            def getGoingOut():
                outs = [set()]*len(self.groups)
                for i,g in enumerate(self.groups):
                    if random.random() <= self.gChance:
                        outs[i] = set(a for a in g if a.willGoOut(self.aChance))
                return outs
            prefs, out = getPreferences(), getGoingOut()
            attendees = [[] for _ in range(self.numRestaurants)]
            for p,g in zip(prefs,out):
                attendees[p].extend([a for a in g])
            return attendees
        attendance = getAttendees()
        self.disease.infect(attendance)
        for g in self.groups:
            for a in g:
                a.passDay(self.disease)
        return attendance
                
    def getSick(self):
        return sum(1 for g in self.groups for a in g if a.isSick())
    
    def getHealthy(self):
        return sum(1 for g in self.groups for a in g if a.isHealthy())
    
    def getDead(self):
        return sum(1 for g in self.groups for a in g if a.isDead())

    def __len__(self):
        return len(self.groups)
    
    def __getitem__(self, i):
        return self.groups[i]
    
    def __setitem__(self,i,v):
        self.groups[i] = v
        
    def __delitem__(self,i):
        self.groups.pop(i)
