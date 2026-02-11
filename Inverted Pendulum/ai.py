import numpy 

class ai:
    def __init__(self, x, v_x, a_c, theta, omega, alpha):
        self.parameters = [x,v_x,a_c,theta,omega,alpha]
        self.F_in = 0  
        self.reward = 0
    
    def decision_tree(self):
        return self.F_in
      



        

