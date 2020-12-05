import numpy as np
import methods as mtd
import random
INPUT_PARAMS = {'weather_condition' : 5 , 'rate_of_spread': 0 , 'restaurant_capacity' : 100 ,'un_employment_rate': 0,  'num_agents' : 100 , 'num_rounds' : 1000}
NUM_STRGY = 100
NUM_RESTAURANTS = 60 #Estimated number of rastaurants in the are
AVG_RESTAURANT_CAP= 40 #average restaurant capacity in the area
#population= 100
class agent:
    def __init__(self, strgy):
        self.strgy = strgy
        self.top_strgy = random.randint(0,9) #giving random strategy the best strategy
        self.top_strgy_score = 0
    def give_best_strgy(self , idx):
        self.top_strgy = idx
    def increase_top_score(self):
        self.top_strgy_score +=1
    def decrease_top_score(self):
        self.top_strgy_score = max(0,self.top_strgy_score-1)
    def cur_predict(self, num):
        self.predicted_going = num
    def get_cur_predict(self):
        return self.predicted_going
    def compute_new_set(self):
        mtd.pram_scale(INPUT_PARAMS)
        self.strgy = mtd.compute_random_strgy(NUM_STRGY, INPUT_PARAMS)


class strgy:
    """docstring for ."""
    def __init__(self, weights):
        self.w = weights
        self.best_score = 0






if __name__ == "__main__":
#this is where the execution starts
    agents = mtd.compute_agent_strgy( NUM_STRGY , INPUT_PARAMS )
    Global_mem = mtd.compute_random_mem(INPUT_PARAMS['num_agents'])#redomly generated memory at the begining
    thrs_hold = mtd.compute_thrshold(INPUT_PARAMS)
    print('threshold is : ', thrs_hold)
    result_arr = []
    for round in range(0,INPUT_PARAMS['num_rounds']):
        #print("round number :", round)
        agent_decision , num_going , num_notgoing = mtd.compute_agent_decision(agents, Global_mem ,thrs_hold)
        #supply agent decisions to sub-team one and obtain the actual agent_decisions
        #you store the num_goint here( it is the variable that tell you how many agents have decided to go out this round)
        winner_loser= mtd.get_winner_loosers( agent_decision, num_going, num_notgoing)
        print("number going : ", num_going )
        #print("number of agnets decision is : ", agent_decision )
        result_arr.append(num_going)
        mtd.compute_new_best(agents,winner_loser, agent_decision, num_going, Global_mem)
        Global_mem.pop()
        Global_mem.insert(0,num_going)
        #print(Global_mem)
    #eric you can take the result_arr from here
