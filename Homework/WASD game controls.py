import pygame
import time
pygame.init()
FPS = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
height = 800
width = 1000
box_x = 300
box_y = 500
box_x_change = 0
box_y_change = 0
speed = 2.5
screen = pygame.display.set_mode((width, height))

while True:
    FPS.tick(100)
    box = pygame.Rect(box_x, box_y, 40, 40)
    pygame.draw.rect(screen, red, box)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                box_x_change = -speed
            if event.key == pygame.K_d:
                box_x_change = speed
            if event.key == pygame.K_w:
                box_y_change = -speed
            if event.key == pygame.K_s:
                box_y_change = speed
        elif event.type == pygame.KEYUP:
            box_x_change = 0
            box_y_change = 0
        box_x += box_x_change
        box_y += box_y_change
        if box_x < 0:
            box_x = 0
        elif box_y < 0:
            box_y = 0
        elif box_x > width - 40:
            box_x = width - 40
        elif box_y > height - 40:
            box_y = height - 40

    pygame.display.update()
    screen.fill(black)
