import classes as cl
import ai 
import time
import pygame
import sys

if __name__ == "__main__":
    my_ai = ai.ai(0,0,0,0,0,0)
    my_game = cl.game()
    running = True
    n = 0
    while running:
        my_game.t = n*my_game.dt
        n+=1
        print('Timestamp: {:.3}'.format(my_game.t))
        #print(f"ball t: {self.ball.theta}")
        running = my_game.handle_events()
        my_game.check_bounds()
        my_game.update()
        my_game.draw()
        reward = my_game.get_reward()
        print(f"Reward: {reward}")
        my_game.clock.tick(60)
    pygame.quit()
    sys.exit()
