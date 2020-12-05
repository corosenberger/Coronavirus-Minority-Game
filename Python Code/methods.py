import numpy as np
import start as st
import random

#this basically decides how each agen t will make decision
Mem = 6
def pram_scale(Input_param):

    Input_param['weather_condition'] = ((Input_param['weather_condition']*2)/10)
    Input_param['restaurant_capacity'] = Input_param['restaurant_capacity']/100
    Input_param['rate_of_spread'] = ((Input_param['rate_of_spread'])/3.5)    #3.5 is the max rate of spread reproted so far


def get_random_weight(Input_param):

    n = 1#0 if random.randint(0,9) <3 else 1
    w1 = random.randint(-1,1)*  (0.99- Input_param['weather_condition']* (random.randint(20,100 )/100))
    #print('weather_condition',w1)
    n = 1#0 if random.randint(0,9) <6 else 1
    w2 =  random.randint(-1,1)* Input_param['restaurant_capacity']* (random.randint(30, 100)/100)
    #print('restaurant_capacity',w2)
    #print('w3', int(2+ Input_param['rate_of_spread']*100))
    n = 1#0 if random.randint(0,9) >4 else 1
    w3 = random.randint(-1,1) * Input_param['rate_of_spread']*(random.randint(60,100)/100)#int(1+ Input_param['rate_of_spread']*100))/100)
    #print('rate_of_spread',w3)
    n = 1#0 if random.randint(0,9) >6 else 1
    w4 = random.randint(-1,1)* Input_param['un_employment_rate']*(random.randint(1,100)/100)
    #print('un_employment_rate',w4)
    final_num = ((w1+w2-w3-w4)/2)
    if(final_num<0):
        return 0
    return final_num

def compute_random_strgy(NUM_STRGY, Input_param):

    strgy_lst = []
    for _ in range(0,NUM_STRGY):
        temp = []
        for _ in range(0, Mem):
            temp.append(get_random_weight(Input_param) )
        strgy_lst.append(temp)
    #print("agent strategy list is: " ,strgy_lst)
    #print("strategy", strgy_lst)
    return strgy_lst

def compute_agent_strgy(NUM_STRGY , Input_param):
    pram_scale(Input_param)
    #print(Input_param)
    agent_list = []
    for agent in range(0,Input_param['numAgents']):
        agent_list.append(st.agent(compute_random_strgy(NUM_STRGY , Input_param)))
    return agent_list


def compute_random_mem(population):
    return[random.randint(0,population) for _ in range(0,Mem) ]



def compute_thrshold_num(Input_param):
    print('threshold', (1.19- Input_param['weather_condition'])+Input_param['restaurant_capacity']-Input_param['rate_of_spread']-Input_param['un_employment_rate'])
    return ((1.19-Input_param['weather_condition'])+Input_param['restaurant_capacity']-Input_param['rate_of_spread']-Input_param['un_employment_rate'])/2

def compute_thrshold( Input_param):
    #print(rst_capacity)
    return  int(Input_param['num_agents']* compute_thrshold_num(Input_param))

def compute_agent_decision(agents, Global_mem ,thrs_hold):
    agent_decisions = []
    num_going = 0
    num_notgoing = 0
    for agent in agents:
        opt_strgy = agent.strgy[agent.top_strgy]
        #print(opt_strgy)
        expected_turnout = 0
        for i in range(0,len(opt_strgy)):
            expected_turnout += opt_strgy[i]*Global_mem[i]


        #print("expected turnout" ,int(expected_turnout*(1/len(opt_strgy))))
        #print("threshold", thrs_hold)
        agent.cur_predict(int(expected_turnout))
        #print("expected turnout" , int(expected_turnout))
        if( expected_turnout < thrs_hold):
            agent_decisions.append(1)
            num_going +=1
        else:
            agent_decisions.append(0)
            num_notgoing +=1
    return agent_decisions , num_going ,num_notgoing



def get_winner_loosers( agent_decision, num_going, num_notgoing):
    not_g = False
    g = False
    win_lose_arr =[]
    if( num_notgoing > num_going):
        g = True
    else:
        not_g = True
    if( not_g is True):
        num_winner = num_notgoing
        for i in range(0,len(agent_decision)):
            if( agent_decision[i]==0):
                win_lose_arr.append(1)
            else:
                win_lose_arr.append(0)

    if(g==True):
        win_lose_arr = agent_decision.copy()
    return win_lose_arr

def get_one_agent_decision(strgy, mem):
    going_val = 0
    for i in range(0,len(strgy)):
         going_val += strgy[i]*mem[i]
    return going_val


def get_new_top_strgy(agent, agent_decision, num_going, Global_mem):
    agent.compute_new_set()
    best_strgy = agent.top_strgy
    cur_prd = abs(num_going - agent.get_cur_predict())

    for i in range(0, len(agent.strgy)):
        #if( agent.top_strgy == i):
        #    continue
        tmp_val = get_one_agent_decision(agent.strgy[i] , Global_mem)
        if( abs(num_going - tmp_val) < cur_prd ):
            cur_prd = abs(num_going - tmp_val)
            best_strgy = i
    #if(best_strgy != agent.top_strgy):
    agent.give_best_strgy(best_strgy)
        #print("next best changed to strgy:" , best_strgy)


def compute_new_best(agents,winner_loser, agents_decision, num_going, Global_mem):
    i = 0
    for agent in agents:
        tmp_result = winner_loser[i]
        if(tmp_result == 1):
            agent.increase_top_score()
        if(tmp_result == 0):
            if(agent.top_strgy_score ==0):
                get_new_top_strgy(agent, agents_decision[i], num_going, Global_mem)
            else:
                agent.decrease_top_score()
        i+=1
        #print("i is :" ,i)
