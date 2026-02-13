import classes as cl
import agents as a
import time
import pygame
import sys
import utils

if __name__ == "__main__":
    #my_ai = a.Random()
    my_ai = a.Scale(-1, 1)
    my_game = cl.game()
    running = True
    n = 0
    reward = 0
    while running:
        my_game.t = n*my_game.dt
        n+=1
        print('Timestamp: {:.3}'.format(my_game.t))
        #print(f"ball t: {self.ball.theta}")
        running = my_game.handle_events()
        my_game.check_bounds()
        my_game.update()
        my_game.draw()

        params = my_game.get_params()
        #print(f"Params {params}")
        reward = my_game.get_reward()
        print(f"Reward: {reward}")

        action = my_ai.get_policy(params)
        my_ai.reinforce(reward)

        print(f"Action: {action}")
        my_game.action(action)
        
        my_game.clock.tick(60)
    pygame.quit()
    sys.exit()
