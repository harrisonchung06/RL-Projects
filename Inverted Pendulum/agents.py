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
    
class Scale:
    def __init__(self, cap):
        self.cap = cap
        self.params = []
        self.action = 0
        self.reward = []
        self.step = 0.01
        self.hyp = random.randint(0, 1)
    def get_policy(self, params):
        self.params = params
        return utils.clamp(-self.params[3]*self.hyp, self.cap)
    def reinforce(self, reward_curr):
        self.reward_prev = self.rewards[-1]
        self.rewards.append(reward_curr)
        if self.reward_prev > reward_curr:
            dir = random.randint(-1,1)
            self.hyp += dir*self.step

class DecisionTree:
    def __init__(self):
        self.params = []
        self.action = 0
        self.reward = []
        self.step = 0.001
        self.dirs = []
        self.hyp = [random.randint(0,1) for _ in range(0,6)]

    def get_policy(self, params):
        self.params = params
        print(self.reward)
        print(self.params)
        print(self.hyp)

        if self.params[0] > self.hyp[0]*self.params[0]:
            if self.params[1] > self.hyp[1]*self.params[1]:
                if self.params[2] > self.hyp[2]*self.params[2]:
                    return 1 
        return 0
    
    def reinforce(self, reward_curr):
        self.reward_prev = self.rewards[-1]
        self.rewards.append(reward_curr)
        if self.reward_prev > reward_curr:
            for hyp in self.hyps:
                self.dirs.append(random.randint(-1,1))
                hyp += self.dirs[-1]*self.step

class PSO:
    def __init__(self):
        pass

    def get_policy(self, params, reward):
        pass

    def improve(self):
        pass #Does something... 
    
class OtherAI:
    def __init__(self):
        pass

    def get_policy(self, params, reward):
        pass

    def improve(self):
        pass #Does something... 

        
    
    



        

