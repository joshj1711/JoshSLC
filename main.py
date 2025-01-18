import threading
import pygame
import sys
from sys import exit

# Initialize Pygame
pygame.init()

# Set up the screen and clock
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((800, 700))
bg = pygame.image.load("pics/pixilart-drawing (31).png")
# Player 1 setup
player1 = pygame.image.load("pics/left.png")
p_x = 100
p_y = 100
player1_rect = player1.get_rect(topright=(p_x, p_y))
player_side = "right"
bullet = pygame.Surface((10, 10))
bullet.fill("black")
bullet_rect = bullet.get_rect(topright=(player1_rect.x, player1_rect.y))
bullet_present = False

# Walls setup
wall1 = pygame.Surface((50, 700))
wall1.fill("red")
wall1_rect = wall1.get_rect(topright=(850, 0))

wall2 = pygame.Surface((50, 700))
wall2.fill("red")
wall2_rect = wall2.get_rect(topright=(0, 0))

wall3 = pygame.Surface((800, 50))
wall3.fill("red")
wall3_rect = wall3.get_rect(topright=(800, -50))

wall4 = pygame.Surface((800, 50))
wall4.fill("red")
wall4_rect = wall4.get_rect(topright=(800, 700))

# Player 2 setup
player_2 = pygame.image.load("pics/left2.png")
player_2_rect = player_2.get_rect(topright=(700, 600))
bullet2 = pygame.Surface((10, 10))
bullet2.fill("black")
bullet_rect2 = bullet2.get_rect(topright=(player_2_rect.x - 10, player_2_rect.y))
bullet2_present = False
player_2side = "left"

# Health variables
health2 = 100
health = 100
FONT = pygame.font.Font(None, 48)
health2_text = str(health2)
health2_surf = FONT.render(health2_text, True, "white")
health2_surf_rect = health2_surf.get_rect(topright=(700, 20))

health_text = str(health)
health1_surf = FONT.render(health_text, True, "white")
health1_surf_rect = health1_surf.get_rect(topright=(100, 20))

# Game over flags
GAME_OVER_2 = ("GAME OVER / PLAYER 1 WINS")
GAME_OVER_2_surf = FONT.render(GAME_OVER_2, True, "white")
GAME_OVER_2_surf_rect = GAME_OVER_2_surf.get_rect(topright=(600, 300))

GAME_OVER = ("GAME OVER / PLAYER 2 WINS")
GAME_OVER_surf = FONT.render(GAME_OVER, True, "white")
GAME_OVER_surf_rect = GAME_OVER_surf.get_rect(topright=(600, 300))

game_over = False

# Main game loop
while True:
    moving = False
    screen.fill("black")
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if health2 <= 0:
            screen.blit(GAME_OVER_2_surf, GAME_OVER_2_surf_rect)
            game_over = True
    if health <= 0:
            screen.blit(GAME_OVER_surf, GAME_OVER_surf_rect)
            game_over = True
    if game_over:
        home_text = "Press The Home Button To Exit"
        home_text_surf = FONT.render(home_text, True, "white")
        home_text_surf_rect = home_text_surf.get_rect(topright=(600, 350))
        screen.blit(home_text_surf, home_text_surf_rect)

        if keys[pygame.K_HOME]:
            pygame.quit()
            exit()

    else:
        # Player 1 movement
        if keys[pygame.K_d]:
            player1_rect.x += 7
            player_side = "right"
            moving = True
        if keys[pygame.K_a]:
            player1_rect.x -= 7
            player_side = "left"
            moving = True
        if keys[pygame.K_w]:
            player1_rect.y -= 7
            player_side = "up"
            moving = True
        if keys[pygame.K_s]:
            player1_rect.y += 7
            player_side = "down"
            moving = True

        # Bullet 1 shooting
        if keys[pygame.K_SPACE] and not bullet_present:
            bullet_present = True
            bullet.fill("yellow")
            bullet_rect.x = player1_rect.x + player1_rect.width // 2 - bullet_rect.width // 2
            bullet_rect.y = player1_rect.y + player1_rect.height // 2 - bullet_rect.height // 2
            bullet_direction = player_side

        # Bullet movement and collisions (Player 1)
        if bullet_present:
            if bullet_direction == "right":
                bullet_rect.x += 20
            if bullet_direction == "left":
                bullet_rect.x -= 20
            if bullet_direction == "up":
                bullet_rect.y -= 20
            if bullet_direction == "down":
                bullet_rect.y += 20

            # Bullet collision with walls
            if bullet_rect.colliderect(wall1_rect) or bullet_rect.colliderect(wall2_rect) or bullet_rect.colliderect(wall3_rect) or bullet_rect.colliderect(wall4_rect):
                bullet_present = False

        # Collision checks for player 1 with walls
        if player1_rect.colliderect(wall1_rect):
            player1_rect.x = 770
        if player1_rect.colliderect(wall2_rect):
            player1_rect.x = 0
        if player1_rect.colliderect(wall3_rect):
            player1_rect.y = 0
        if player1_rect.colliderect(wall4_rect):
            player1_rect.y = 670

        # Bullet collision with player 2
        if bullet_rect.colliderect(player_2_rect):
            health2 -= 5

        # Player 2 movement
        if keys[pygame.K_LEFT]:
            player_2_rect.x -= 7
            player_2side = "left"
            moving = True
        if keys[pygame.K_RIGHT]:
            player_2_rect.x += 7
            player_2side = "right"
            moving = True
        if keys[pygame.K_DOWN]:
            player_2_rect.y += 7
            player_2side = "down"
            moving = True
        if keys[pygame.K_UP]:
            player_2_rect.y -= 7
            player_2side = "up"
            moving = True


        if keys[pygame.K_SLASH] and not bullet2_present:
            bullet2_present = True
            bullet2.fill("yellow")
            bullet_rect2.x = player_2_rect.x + player_2_rect.width // 2 - bullet_rect2.width // 2
            bullet_rect2.y = player_2_rect.y + player_2_rect.height // 2 - bullet_rect2.height // 2
            bullet_direction2 = player_2side


        if bullet2_present:
            if bullet_direction2 == "right":
                bullet_rect2.x += 20
            if bullet_direction2 == "left":
                bullet_rect2.x -= 20
            if bullet_direction2 == "up":
                bullet_rect2.y -= 20
            if bullet_direction2 == "down":
                bullet_rect2.y += 20


            if bullet_rect2.colliderect(wall1_rect) or bullet_rect2.colliderect(wall2_rect) or bullet_rect2.colliderect(wall3_rect) or bullet_rect2.colliderect(wall4_rect):
                bullet2_present = False
        if health <= 0:
            game_over = False

        if player_2_rect.colliderect(wall1_rect):
            player_2_rect.x = 770
        if player_2_rect.colliderect(wall2_rect):
            player_2_rect.x = 0
        if player_2_rect.colliderect(wall3_rect):
            player_2_rect.y = 0
        if player_2_rect.colliderect(wall4_rect):
            player_2_rect.y = 670

        if bullet_rect2.colliderect(player1_rect):
            health -= 5


        if player_side == "right":
            player1 = pygame.image.load("pics/right.png")
        elif player_side == "left":
            player1 = pygame.image.load("pics/left.png")
        elif player_side == "up":
            player1 = pygame.image.load("pics/up.png")
        elif player_side == "down":
            player1 = pygame.image.load("pics/down.png")

        if player_2side == "down":
            player_2 = pygame.image.load("pics/down2.png")
        elif player_2side == "up":
            player_2 = pygame.image.load("pics/up2.png")
        elif player_2side == "right":
            player_2 = pygame.image.load("pics/right2.png")
        elif player_2side == "left":
            player_2 = pygame.image.load("pics/left2.png")

        health2_text = str(health2)
        health2_surf = FONT.render(health2_text, True, "white")
        health2_surf_rect = health2_surf.get_rect(topright=(700, 20))

        health_text = str(health)
        health1_surf = FONT.render(health_text, True, "white")
        health1_surf_rect = health1_surf.get_rect(topright=(100, 20))



        screen.blit(bullet, bullet_rect)
        screen.blit(bullet2, bullet_rect2)
        screen.blit(player_2, player_2_rect)
        screen.blit(player1, player1_rect)
        screen.blit(wall2, wall2_rect)
        screen.blit(wall1, wall1_rect)
        screen.blit(wall3, wall3_rect)
        screen.blit(wall4, wall4_rect)
        screen.blit(health2_surf, health2_surf_rect)
        screen.blit(health1_surf, health1_surf_rect)

    pygame.display.update()
    CLOCK.tick(60)
