import pygame
import time

def snakegame():
    pygame.init()

    white = (255, 255, 255) # screen
    black=(0,0,0)           # snake
    red=(255,0,0)           # food

    # game window
    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption("Snake Game by Griffin")

    # display
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_block = 10

    clock = pygame.time.Clock()
    snake_speed = 30

    # exit message 'you lost'
    font_style = pygame.font.SysFont(None, 50)
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width/2, dis_height/2])

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
        # border block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
 
        # update move snake
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block]) # snake
        
        pygame.display.update()

        clock.tick(snake_speed)

    message("you lost", red)
    pygame.display.update()
    time.sleep(2)

    # exit
    pygame.quit()
    quit()


if __name__ == "__main__":
    snakegame()
