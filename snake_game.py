import pygame

# from pygame.locals import *


def snakegame():
    pygame.init()

    white = (255, 255, 255) # screen
    black=(0,0,0)          # snake
    red=(255,0,0)           # blocks

    x1 = 300
    y1 = 300
    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()

    # game window
    dis = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake Game by Griffin")

    # pygame.display.update()

    # prev auto quit
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            # close on x
            if event.type == pygame.QUIT: 
                game_over = True
            # move snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, 10, 10]) # snake
        
        pygame.display.update()

        clock.tick(30)



    # exit
    pygame.quit()
    quit()


if __name__ == "__main__":
    snakegame()
