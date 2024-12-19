import pygame
import sys
import random

WHITE = (255, 255, 255)
GREEN = (117, 217,2)
BLUE = (0,0,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

square_x = screen_width/2
square_y = screen_height/2
square_size = 10

treasure_x = random.randrange(0, screen_width)
treasure_y = random.randrange(0, screen_height)
treasure_size = 50

enemy_size = 50
enemy_x = enemy_size
enemy_y = enemy_size

bullets = []
bullet_size = 100
bullet_speed = 5

score = 0

shoot_cooldown = 1_000
game_time = 60
shoot_time = pygame.time.get_ticks() - shoot_cooldown
start_ticks = pygame.time.get_ticks()
clock = pygame.time.Clock()

def shoot_bullet(direction):
    global shoot_time
    now = pygame.time.get_ticks()
    if now - shoot_time > shoot_cooldown:
        bullets.append([square_x, square_y, direction])
        shoot_time = pygame.time.get_ticks()


def move_bullets():
    for bullet in bullets:
        if bullet[2] == "up":
            bullet[1] -= bullet_speed
        elif bullet[2] == "down":
            bullet[1] += bullet_speed
        elif bullet[2] == "left":
            bullet[0] -= bullet_speed
        elif bullet[2] == "right":
            bullet[0] += bullet_speed

def draw_bullets():
    for bullet in bullets:
        if bullet[2] == "up" or bullet[2] == "down":
            pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], bullet_size/3, bullet_size))
        elif bullet[2] == "left" or bullet[2] == "rigth":
            pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], bullet_size, bullet_size/3))


running = True
while running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame:quit()
            sys.exit()
    pygame.time.Clock().tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        square_x = square_x - 50
    if keys[pygame.K_d]:
        square_x = square_x + 50
    if keys[pygame.K_w]:
        square_y = square_y - 50
    if keys[pygame.K_s]:
        square_y = square_y + 50
    if keys[pygame.K_SPACE]:
        shoot_bullet()
    if keys[pygame.K_LEFT]:
        shoot_bullet("left")
    if keys[pygame.K_RIGHT]:
        shoot_bullet("right")
    if keys[pygame.K_UP]:
        shoot_bullet("up")
    if keys[pygame.K_DOWN]:
        shoot_bullet("down")



    if  square_x > enemy_x:
        enemy_x += 50
    if  square_x < enemy_x:
        enemy_x -= 50
    if  square_y > enemy_y:
        enemy_y += 50
    if  square_y < enemy_y:
        enemy_y -= 50

    if square_x < treasure_x + treasure_size and square_x > treasure_x - treasure_size and square_y < treasure_y + treasure_size and square_y > treasure_y - treasure_size:
        treasure_x = random.randrange(0, screen_width)
        treasure_y = random.randrange(0, screen_height) 
        score += 1

    if square_x < enemy_x + enemy_size and square_x > enemy_x - enemy_size and square_y < enemy_y + enemy_size and square_y > enemy_y - enemy_size:
        enemy_x = random.randrange(0, screen_width)
        enemy_y = random.randrange(0, screen_height) 
        score -= 1

    for bullet in bullets:
        if bullet[0] < enemy_x + enemy_size and bullet[0] > enemy_x - enemy_size and bullet[1] < enemy_y + enemy_size and bullet[1] > enemy_y - enemy_size:
            enemy_x = random.randrange(0, screen_width)
            enemy_y = random.randrange(0, screen_height) 
            score += 1

    if score < -100:
        running = False

    playing_time = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = game_time - playing_time
    if time_left <= 0:
        running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))
    pygame.draw.circle(screen, GREEN, (treasure_x, treasure_y), treasure_size, 100)
    pygame.draw.circle(screen, RED, (enemy_x, enemy_y), enemy_size, 100)
    draw_bullets()
    move_bullets()

    font = pygame.font.SysFont("microsoft", 35)
    time_text = font.render(f"Tiempo XD: {time_left}", True, BLACK)
    screen.blit(time_text, (10, 50))
    score_text = font.render(f"Monedas: {score}", True, BLACK)
    screen.blit(score_text, (10, 20))
    pygame.display.flip()