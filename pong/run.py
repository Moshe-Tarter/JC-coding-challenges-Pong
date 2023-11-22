import pygame as pg
import sys

# setup and vars
pg.init()
screen = pg.display.set_mode((1300, 500))
clock = pg.time.Clock()
game_active = False
single_player = False
ball_x_direction, ball_y_direction = 6, 2
player1_score, player2_score = 0, 0


def update_score():
    player1_score_card_surf = text_font.render(f'{player1_score}', False, 'Red')
    player2_score_card_surf = text_font.render(f'{player2_score}', False, 'Red')
    player1_score_rect = player1_score_card_surf.get_rect(center=(600, 100))
    player2_score_rect = player1_score_card_surf.get_rect(center=(700, 100))
    screen.blit(player1_score_card_surf, player1_score_rect)
    screen.blit(player2_score_card_surf, player2_score_rect)
    
    
def oppenent():
    if player1_rect.bottom <= 500 and player1_rect.top >= 0:
        player1_rect.centery = ball_rect.y
    elif player1_rect.bottom > 500:
        player1_rect.bottom = 498
    else:
        player1_rect.top = 2
        
        
def handle_input():
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and player2_rect.top > 0:
        player2_rect.y -= 4
        
    if keys[pg.K_DOWN] and player2_rect.bottom < 500:
        player2_rect.y += 4
        
    if keys[pg.K_w] and player1_rect.top > 0:
        player1_rect.y -= 4
        
    if keys[pg.K_s] and player1_rect.bottom < 500:
        player1_rect.y += 4


text_font = pg.font.Font('pong/resources/font/Pixeltype.ttf', 80)
player1_surf = pg.image.load('pong/resources/Paddle.png').convert_alpha()
player2_surf = pg.image.load('pong/resources/Paddle.png').convert_alpha()
ball_surf = pg.image.load('pong/resources/Ball.png').convert_alpha()
game_over_surface = text_font.render('PONG', False, 'Red').convert_alpha()
new_game_surf = text_font.render('Press Space To Start A New Game!', False, 'Red')
options_surf_single = text_font.render(f'1. For Single Player Mode', False, 'Red')
options_surf_multi = text_font.render('2. For 2 players Mode', False, 'Red')

player1_rect = player1_surf.get_rect(center=(20, 250))
player2_rect = player2_surf.get_rect(center=(1280, 250))
ball_rect = ball_surf.get_rect(center=(650, 250))
game_over_rect = game_over_surface.get_rect(midbottom=(650, 100))
new_game_rect = new_game_surf.get_rect(midbottom=(650, 400))
options_single_rect = options_surf_single.get_rect(midbottom=(650, 350))
options_multi_rect = options_surf_multi.get_rect(midbottom=(650, 450))

while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    screen.fill((0, 0, 0))
    pg.draw.line(screen, 'Red', start_pos=(650, 0), end_pos=(650, 500))
    screen.blit(player1_surf, player1_rect)
    screen.blit(player2_surf, player2_rect)
    screen.blit(ball_surf, ball_rect)
    

        
    if game_active:

        handle_input()
        update_score()
        
        if single_player:
            oppenent()

        # ball logic
        ball_rect.x += ball_x_direction
        ball_rect.y += ball_y_direction
        if player1_rect.colliderect(ball_rect):
            print('collision ball and player 1')
            ball_x_direction *= -1
        if player2_rect.colliderect(ball_rect):
            print('collision ball and player 2')
            ball_x_direction *= -1
        if ball_rect.top < 0 or ball_rect.bottom > 495:
            print('ball is outside of board')
            ball_y_direction *= -1
        if ball_rect.x < 0:
            player2_score += 1
            ball_rect.x = 650
            ball_rect.y = 250
            update_score()
        if ball_rect.x > 1300:
            player1_score += 1
            ball_rect.x = 650
            ball_rect.y = 250
            update_score()
        if player1_score == 5 or player2_score == 5:
            game_active = False   
                    
    else:
        screen.fill('Black')
        screen.blit(game_over_surface, game_over_rect)
        screen.blit(options_surf_single, options_single_rect)
        screen.blit(options_surf_multi, options_multi_rect)
        keys = pg.key.get_pressed()
        if keys[pg.K_1]:
            player1_score, player2_score = 0, 0
            single_player = True
            game_active = True
            
        if keys[pg.K_2]:
            player1_score, player2_score = 0, 0
            single_player = False
            game_active = True

    pg.display.flip()
    clock.tick(60)
    