import numpy 
import random
import utils

#No reinforcement:
class Random:
    def __init__(self):
        self.params = []
        self.action = 0
        self.reward = 0
    def get_policy(self, params):
        return random.randint(-1,1)

#Linear Regression Agent
class Linear:
    def __init__(self, cap_min, cap_max):
        self.cap_min = cap_min
        self.cap_max = cap_max
        self.params = []
        self.action = 0
        self.rewards = [0]
        self.step = 0.2
        self.hyps = [random.randint(-1, 1) for _ in range(6)]
    def get_policy(self, params): #Kernel
        print(self.hyps)
        self.params = params
        s=0
        for i in range(len(self.params)):
            s += self.params[i]*self.hyps[i]
        return utils.clamp(s, self.cap_min, self.cap_max)
    def reinforce(self, reward_curr): #Optimization (Monte Carlo)
        self.reward_prev = self.rewards[-1]
        self.rewards.append(reward_curr)
        if self.reward_prev > reward_curr:
            for i in range(len(self.hyps)):
                self.hyps[i] += random.randint(-1,1)*self.step

class OtherAI:
    def __init__(self):
        pass

    def get_policy(self, params, reward):
        pass

    def improve(self):
        pass #Does something... 

        
    
    



        

