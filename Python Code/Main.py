import Disease
import Group

def main(inputs):
    disease = Disease.Disease(inputs['startSickChance'],inputs['startSymptomaticChance'],
        inputs['rateOfSpread'],inputs['sickTime'],inputs['incubationTime'],inputs['immuneTime'])
    groups = Group.Groups(inputs['numGroups'],inputs['numAgents'],inputs['numRestaurants'],
        inputs['gChance'],inputs['aChance'],disease)
    sick, healthy, winners = {}, {}, {}
    
    for i in range(inputs['numDays']):
        sick[i] = groups.getSick()
        healthy[i] = groups.getHealthy()
        groups.passDay()
        winners[i] = sum(1 for v in groups.getWinners() if v)

    return sick,healthy,winners

if __name__ == '__main__':
    inputs = {
        #Disease inputs
        'startSickChance': 0.01,
        'startSymptomaticChance': 0.5,
        'rateOfSpread': 0.01,
        'sickTime': 1,
        'incubationTime': 14,
        'immuneTime': 10,
            
        #Groups inputs
        'numGroups': 2000,
        'numAgents': 10000,
        'numRestaurants': 10,
        'gChance': 0.1,
        'aChance': 0.5,
            
        'numDays': 1000
    }
    main(inputs)
