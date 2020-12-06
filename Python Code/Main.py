import Disease
import Group
import methods as mtd
import numpy as np
import random

NUM_STRGY = 100
AVG_RESTAURANT_CAP= 40

def main(inputs):
    disease = Disease.Disease(inputs['startSickChance'],inputs['startSymptomaticChance'],
        inputs['rateOfSpread'],inputs['sickTime'],inputs['incubationTime'],inputs['immuneTime'])
    groups = Group.Groups(inputs['numGroups'],inputs['numAgents'],inputs['numRestaurants'],disease)
    
    agents = mtd.compute_agent_strgy(NUM_STRGY , inputs)
    Global_mem = mtd.compute_random_mem(inputs['num_agents']) #redomly generated memory at the begining
    thrs_hold = mtd.compute_thrshold(inputs)
    
    sick, healthy, attendance = {}, {}, {}

    for i in range(inputs['numDays']):
        sick[i] = groups.getSick()
        healthy[i] = groups.getHealthy()

        agent_decision, num_going, _ = mtd.compute_agent_decision(agents, Global_mem , thrs_hold)
        atdn = groups.passDay(agent_decision)
        winner_loser = groups.getWinners()
        mtd.compute_new_best(agents, winner_loser, agent_decision, num_going, Global_mem)
        Global_mem.pop()
        Global_mem.insert(0,num_going)

        attendance[i] = sum(len(g) for r in atdn for g in r)

    

    return sick,healthy,attendance

if __name__ == '__main__':
    inputs = {
        #Disease inputs
        'startSickChance': 0.01,
        'startSymptomaticChance': 0.5,
        'rateOfSpread': 1,
        'sickTime': 1,
        'incubationTime': 14,
        'immuneTime': 10,
            
        #Groups inputs
        'numGroups': 2000,
        'numAgents': 10000,
        'numRestaurants': 10,
            
        'numDays': 1000,

        #Sub-team 2 Inputs
        'weather_condition': 5,
        'rate_of_spread': 1,
        'restaurant_capacity': 100,
        'un_employment_rate': 0,
        'num_agents': 10000,
        'num_rounds': 1000
    }
    main(inputs)
