import PythonC.GroupC as gc
import Disease
import Agent
import random

sz = gc.getGroupSizes(1000,200,10)
print(sz)

d = Disease.Disease(0,1,0,1,1,0)
x = [Agent.Agent(d) for _ in range(4)]
for a in x[:2]: a.willGoOut = True
y = gc.getWinners(x)
print([a.willGoOut for a in x])
print([a.isSick() for a in x])
print([a.wonLastRound for a in x])

subteam2input = [random.random() <= 0.5 and a.phase != Agent.SYMPTOMATIC for a in x]
gc.processSubTeam2Input(x,subteam2input)
print(subteam2input)
print([a.willGoOut for a in x])