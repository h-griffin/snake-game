import pygame

# from pygame.locals import *


def snakegame():
    pygame.init()

    # game window
    dis = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Snake Game by Griffin")

    pygame.display.update()

    blue=(0,0,255)
    red=(255,0,0)

    # prev auto quit
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            # close on x
            if event.type == pygame.QUIT: 
                game_over = True
        pygame.draw.rect(dis, blue, [200,150,10,10])
        pygame.display.update()


    # exit
    pygame.quit()
    quit()


if __name__ == "__main__":
    snakegame()


# import pygame
# pygame.init()
# dis=pygame.display.set_mode((400,300))
 
# pygame.display.set_caption('Snake game by Edureka')
 
# blue=(0,0,255)
# red=(255,0,0)
 
# game_over=False
# while not game_over:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             game_over=True
#     pygame.draw.rect(dis,blue,[200,150,10,10])
#     pygame.display.update()
# pygame.quit()
# quit()