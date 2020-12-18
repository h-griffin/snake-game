import pygame
import time
import random

def snakegame():
    """game logic container, message(), rules(), our_snake(), your_score(), game_loop() """
    pygame.init()

    white = (255, 255, 255) # screen
    black=(0,0,0)           # snake
    red=(255,0,0)           # message
    blue = (0, 0, 255)      # food
    green = (0, 255, 0)     # score

    # game window
    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption("Snake Game by Griffin")

    clock = pygame.time.Clock()

    # display
    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("bahnschrift", 35)

    # exit message, score
    def message(msg, color):
        """display messages with color preference"""
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 3, dis_height / 2])

    def rules(msg, color):
        """display rules with color preference"""
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 8, dis_height / 4])
    
    def controls(msg, color):
        """display rules with color preference"""
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 3, dis_height / 3])

    def our_snake(snake_block, snake_list):
        """display snake"""
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def your_score(score):
        """display score with color preference"""
        value = score_font.render("Your Score: " + str(score), True, green)
        dis.blit(value, [0, 0])

    def game_loop(): 
        """run game or quit when asked""" 
        # prev auto quit
        game_over = False
        game_close = False
    
        # display
        x1 = dis_width / 2
        y1 = dis_height / 2
        x1_change = 0
        y1_change = 0

        snake_list = []
        snake_length = 1
    
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    
        while not game_over:
            # wait game 
            while game_close == True:
                dis.fill(white)
                your_score(snake_length - 1)
                rules("gather food without hitting the border or your snake body", black)
                controls("WASD or arrow keys", red)
                message("Press Q-Quit or E-Play", red)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:     # play again
                            game_loop()
                        if event.key == pygame.K_q:     # quit
                            game_over = True
                            game_close = False
            # in game
            for event in pygame.event.get():
                # close on x
                if event.type == pygame.QUIT:
                    game_over = True
                # move snake
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        x1_change = 0
                        y1_change = -snake_block
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        x1_change = 0
                        y1_change = snake_block
    
            # border block
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
    
            x1 += x1_change
            y1 += y1_change
            dis.fill(white)
            pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close == True
        
            our_snake(snake_block, snake_list)
            your_score(snake_length - 1)
            pygame.display.update()
        
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_length += 1
            clock.tick(snake_speed)
    
        pygame.quit()
        quit()

    game_loop()

if __name__ == "__main__":
    snakegame()
