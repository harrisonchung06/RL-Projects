import pygame
import numpy as np
import sys
import utils

class game:
    def __init__(self,instance_id = 0, screen_width=800, screen_height=600):
        #parameters 
        self.BOUND = 5 #meters 
        self.SCALE = 100 #scaling in pixels/meter
        self.dt = 0.01 #s 
        self.t = 0 #s

        #pygame setup
        pygame.init()

        self.instance_id = instance_id
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(f"Instance {self.instance_id}")

        self.clock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.BLACK = (0,0,0)

        #objects
        self.cart = cart()     
        self.ball = ball()  
        self.stick = stick(self.ball, self.cart) 

        #energy
        self.e = []
        self.ts = []

    def update(self):
        A = np.array([
            [self.cart.CART_MASS+self.ball.BALL_MASS, self.ball.BALL_MASS*self.ball.L*np.cos(self.ball.theta)],
            [np.cos(self.ball.theta), self.ball.L]
            ])
        B = np.array([self.cart.F_in+self.ball.BALL_MASS*self.ball.omega**2*self.ball.L*np.sin(self.ball.theta), -self.cart.G*np.sin(self.ball.theta)])
        X = np.linalg.solve(A, B)
        a_c, alpha = X
        alpha = -alpha
        self.cart.update(self.dt, a_c)
        self.ball.update(self.dt, alpha)

    def get_reward(self):
        angle_reward =  1/(1-0.9*np.cos(self.ball.theta)) 
        position_reward = - 1/(0.01*(self.cart.x+4.5)**2*(self.cart.x-4.5)**2)
        position_reward = utils.min_cap(position_reward, -20)
        return angle_reward + position_reward

    def get_params(self):
        return [self.cart.x, self.cart.v_x, self.cart.a_c, self.ball.theta, self.ball.omega, self.ball.alpha]
    
    def get_energy(self):
        p_e = self.ball.BALL_MASS*self.ball.G*(self.ball.L*np.cos(self.ball.theta)+self.ball.L)
        k_e = 0.5*self.ball.BALL_MASS*self.ball.L**2*self.ball.omega**2+0.5*(self.ball.BALL_MASS+self.cart.CART_MASS)*self.cart.v_x**2
        self.e.append(p_e+k_e)
        self.ts.append(self.t)
    
    def plot_energy(self):
        utils.plot(self.ts, self.e, "Energy Time Plot", "Time (s)", "Energy (J)")

    def action(self, action):
        self.cart.F_in += action

    def draw(self):
        self.screen.fill(self.BLACK)
        self.cart.draw(self.screen, self.SCALE, self.screen_width//2, self.screen_height//2)
        self.ball.draw(self.screen, self.SCALE, self.screen_width//2, self.screen_height//2, self.cart)
        self.stick.draw(self.screen, self.SCALE, self.screen_width//2, self.screen_height//2)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                #if event.key == pygame.K_RIGHT: #Manual inputs 
                    #self.cart.F_in += 1
                    #print(f"F {self.cart.F_in}")
                #if event.key == pygame.K_LEFT:
                    #self.cart.F_in -= 1
                    #print(f"F {self.cart.F_in}")
            elif event.type == pygame.QUIT:
                return False
        return True

    def check_bounds(self):
        x = int(self.cart.x*self.SCALE+self.screen_width//2-0.5*self.cart.CART_LENGTH*self.SCALE)
        ball_y = int(-self.ball.y*self.SCALE+self.screen_height//2)
        if x <= 0 or x >= self.screen_width-self.cart.CART_LENGTH*self.SCALE:
            self.reset()
        #elif ball_y >= self.screen_height//2:
            #self.reset()

    def reset(self):
        self.t = 0
        self.cart = cart()     
        self.ball = ball()  
        self.stick = stick(self.ball, self.cart) 

class cart:
    def __init__(self, x=0, length=1, color = (255,255,255)):

        #parameters 
        self.CART_LENGTH = length #meters 
        self.CART_HEIGHT = 0.4 #meter
        self.CART_MASS = 5 #kg
        self.G = 10 #m/s^2
        self.CART_COLOR = color #rgb 

        #kinematics 
        self.x,self.y = x,0 #m
        self.F_in = 0 #N
        self.v_x = 0 #m/s
        self.a_c = 0 #m/s^2 

    def update(self, dt, a_c):
        self.a_c = a_c
        self.v_x += self.a_c*dt
        self.x += self.v_x*dt

    def draw(self, screen, scale, offset_x, offset_y):
        pygame.draw.rect(screen, self.CART_COLOR, (int(self.x*scale+offset_x-0.5*self.CART_LENGTH*scale), int(self.y*scale+offset_y-0.5*self.CART_HEIGHT*scale), self.CART_LENGTH*scale, self.CART_HEIGHT*scale))

class ball:
    def __init__(self, theta_start = 0.1, color = (255,255,255)):
        #parameters 
        self.L = 1 #meters 
        self.BALL_MASS = 1 #kg
        self.G = 10 #m/s^2
        self.COLOR = color
        self.radius = 0.1 #meters
        self.theta = theta_start #rad  
        self.omega = 0 #rad/s
        self.alpha = 0 #rad/s^2 

        self.x,self.y = self.L*np.sin(self.theta), self.L*np.cos(self.theta) 

    def update(self, dt, alpha):
        self.alpha = alpha 
        self.omega += self.alpha*dt
        self.theta += self.omega*dt 
        self.x,self.y = self.L*np.sin(self.theta), self.L*np.cos(self.theta)

    def draw(self, screen, scale, offset_x, offset_y, cart):
        pygame.draw.circle(screen, self.COLOR, (int(self.x*scale+cart.x*scale+offset_x), int(-self.y*scale+offset_y)), self.radius*scale)

class stick:
    def __init__(self, ball, cart, color=(255, 255, 255)):
        self.ball = ball
        self.cart = cart
        self.color = color

    def draw(self, screen, scale, offset_x, offset_y):
        cart_center_x = self.cart.x + self.cart.CART_LENGTH // 2
        cart_center_y = self.cart.y + self.cart.CART_HEIGHT // 2

        pygame.draw.line(screen, self.color, (int(self.ball.x*scale+self.cart.x*scale+offset_x), int(-self.ball.y*scale+offset_y)), (int(cart_center_x*scale+offset_x), int(cart_center_y*scale+offset_y)), 5)

