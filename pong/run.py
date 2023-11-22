import pygame as pg
import sys
import random

# setup and vars
pg.init()
screen = pg.display.set_mode((1300, 500))
clock = pg.time.Clock()
game_active = True
player1_y = 250
player2_y = 250
ball_x_direction, ball_y_direction = 3, 2

player1_surf = pg.image.load('pong/resources/Paddle.png').convert_alpha()
player2_surf = pg.image.load('pong/resources/Paddle.png').convert_alpha()
ball_surf = pg.image.load('pong/resources/Ball.png').convert_alpha()

player1_rect = player1_surf.get_rect(center=(20, player1_y))
player2_rect = player2_surf.get_rect(center=(1280, player2_y))
ball_rect = ball_surf.get_rect(center=(650, 250))

while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    screen.fill((0, 0, 0))
    screen.blit(player1_surf, player1_rect)
    screen.blit(player2_surf, player2_rect)
    screen.blit(ball_surf, ball_rect)
    pg.draw.line(screen, 'Red', start_pos=(650, 0), end_pos=(650, 500))
    
    if game_active:
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and player2_rect.top > 0:
            player2_rect.y -= 4
            
        if keys[pg.K_DOWN] and player2_rect.bottom < 500:
            player2_rect.y += 4
            
        if keys[pg.K_w] and player1_rect.top > 0:
            player1_rect.y -= 4
            
        if keys[pg.K_s] and player1_rect.bottom < 500:
            player1_rect.y += 4


        # ball logic
        ball_rect.x += ball_x_direction
        ball_rect.y += ball_y_direction
        if player1_rect.colliderect(ball_rect):
            print('collision ball and player 1')
            ball_x_direction *= -1
        if player2_rect.colliderect(ball_rect):
            print('collision ball and player 2')
            ball_x_direction *= -1
        if ball_rect.y < 0 or ball_rect.y > 495:
            print('ball is outside of board')
            ball_y_direction *= -1
        if ball_rect.x < 0 or ball_rect.x > 1300:
            game_active = False    
                    
    else:
        screen.fill('Black')

    pg.display.flip()
    clock.tick(60)