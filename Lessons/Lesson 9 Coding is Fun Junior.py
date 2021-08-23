import pygame
pygame.init()
clock = pygame.time.Clock()

green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
width = 800
height = 600
box_x_green = 100
box_y_green = 100
box_x_pink = 700
box_y_pink = 100
screen = pygame.display.set_mode((width, height))

while True:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    box1 = pygame.Rect(box_x_green, box_y_green, 40, 40)
    pygame.draw.rect(screen, green, box1)
    pygame.display.update()
    screen.fill(black)
