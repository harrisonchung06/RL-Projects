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
        self.dirs = [random.randint(-1,1)]
        self.dir_curr = 1
        self.step = 0.2
        self.hyps = [random.randint(0, 1) for _ in range(6)]
    def get_policy(self, params):
        print(self.hyps)
        self.params = params
        return utils.clamp(-self.params[3]*self.hyps[0], self.cap_min, self.cap_max)
    def reinforce(self, reward_curr):
        self.reward_prev = self.rewards[-1]
        self.rewards.append(reward_curr)
        self.dir_prev = self.dirs[-1]
        self.dirs.append(self.dir_curr)
        if self.reward_prev > reward_curr:
            self.dir_curr = -1*self.dir_prev
            self.hyps[0] += self.dir_curr*self.step
    
class OtherAI:
    def __init__(self):
        pass

    def get_policy(self, params, reward):
        pass

    def improve(self):
        pass #Does something... 

        
    
    



        

