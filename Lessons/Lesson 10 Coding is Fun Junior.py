import pygame

pygame.init()
FPS_clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')
pygame.display.flip()
game_font = pygame.font.SysFont('Algerian', 20)

pink = (255, 100, 203)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
width = 800
height = 600
player_x = 50
player_y = 50
player_x_change = 0
player_y_change = 0

while True:
    FPS_clock.tick(100)
    speed = 3.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_change = -speed
            if event.key == pygame.K_d:
                player_x_change = speed
            if event.key == pygame.K_w:
                player_y_change = -speed
            if event.key == pygame.K_s:
                player_y_change = speed
        elif event.type == pygame.KEYUP:
            player_x_change = 0
            player_y_change = 0

    player_x += player_x_change
    player_y += player_y_change

    if player_x < 0:
        player_x = 0
    elif player_y < 0:
        player_y = 0
    elif player_x > width - 20:
        player_x = width - 20
    elif player_y > height - 20:
        player_y = height - 20

    player_controlled = pygame.Rect(player_x, player_y, 30, 30)
    green_blob = pygame.Rect(250, 200, 300, 75)
    if player_controlled.colliderect(green_blob):
        pygame.draw.rect(screen, blue, green_blob)
        collision_detector = game_font.render("Overlapping: VERBoverlapping (present participle)extend over so as to cover partly.the canopy overlaps the house roof at one end · [more]ynonyms:double · double over · double up · crease · turn under · turn up · turn over · bend · tuck · gather ·pleat · crimp · bunchcover part of the same area of interest, responsibility, etc..their duties sometimes overlappedsynonyms:spread (out) · space (out) · time at intervalspartlycoincide in time.'wo new series overlapped, False, green", False, green)
        screen.blit(collision_detector, (100, 100))
    else:
        pygame.draw.rect(screen, green, green_blob)
    pygame.draw.rect(screen, pink, player_controlled)
    pygame.display.update()
    screen.fill(black)
