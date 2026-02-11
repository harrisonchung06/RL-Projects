import numpy 
import random

class Random:
    def __init__(self):
        self.params = []
        self.action = 0
        self.reward = 0
    def get_policy(self, params):
        return random.randint(-1,1)

class DecisionTree:
    def __init__(self):
        self.params = []
        self.action = 0
        self.reward = 0
        self.step = 0.001
        self.hyp = [random.randint(0,1) for _ in range(0,3)]

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
    
    def reinforce(self, reward):
        pass
    
class OtherAI:
    def __init__(self):
        pass

    def get_policy(self, params, reward):
        pass

    def improve(self):
        pass #Does something... 

        
    
    



        

