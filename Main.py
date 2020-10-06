import Disease
import Group
from matplotlib import pyplot as plt

numRestaurants = 10

def main(numGroups=2000,numAgents=10000):
    groups = Group.initPopulations(numGroups,numAgents,numRestaurants)
    sick, healthy, dead = {}, {}, {}
    
    for i in range(1000):
        prefs = Group.getPreferences(groups,numRestaurants)
        out = Group.getGoingOut(groups)
        attendees = Group.getAttendees(prefs,out,numRestaurants)
        
        sick[i] = sum(1 for g in groups for a in g if a.isSick())
        healthy[i] = sum(1 for g in groups for a in g if a.isHealthy())
        dead[i] = sum(1 for g in groups for a in g if a.isDead())
        Disease.infect(attendees)
        Group.passDay(groups)
        
    x = list(sick.keys())
    y = list((a,b,c) for a,b,c in zip(sick.values(),healthy.values(),dead.values()))
    plt.plot(x,y)

if __name__ == '__main__':
    main()