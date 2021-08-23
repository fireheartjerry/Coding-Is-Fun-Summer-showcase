import pygame
# starting variables
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# info and difficulty selector.
start = input("\033[1;32mWelcome to MAZE pygame, in this game your goal is to get to the other side of the window. \nif you touch red, you will die! Controls are standard WASD. \npress any key to continue: ")
difficulty = eval(input("Choose a difficulty, the higher the number, the harder it is(1-4) "))

# beginning of pygame
pygame.init()

# special variables
FPS_clock = pygame.time.Clock()
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game - Touch red and DIE")

game_font = pygame.font.SysFont('Impact', 40)
screen.fill(black)


# main() as function for starter
def main(speed, player_x, player_y, player_x_change, player_y_change):
    while True:
        FPS_clock.tick(100)
        for event in pygame.event.get():

            # WASD controls and events
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

            # Does nothing if no keys are pressed
            elif event.type == pygame.KEYUP:
                player_x_change = 0
                player_y_change = 0

        # movement mechanism
        player_x += player_x_change
        player_y += player_y_change

        # border detection
        if player_x < 0:
            player_x = 0
        elif player_y < 0:
            player_y = 0
        elif player_x > width - 15:
            player_x = width - 15
        elif player_y > height - 15:
            player_y = height - 15

        # initiation of player
        player_controlled = pygame.Rect(player_x, player_y, 15, 15)
        pygame.draw.rect(screen, white, player_controlled)

        # defining walls
        wall1 = pygame.Rect(25, 0, 20, 540)
        wall2 = pygame.Rect(70, 0, 20, 200)
        wall3 = pygame.Rect(70, 230, 20, 375)
        wall4 = pygame.Rect(115, 0, 20, 200)
        wall5 = pygame.Rect(115, 0, 20, 540)
        wall6 = pygame.Rect(160, 0, 20, 200)
        wall7 = pygame.Rect(160, 230, 20, 375)
        wall8 = pygame.Rect(205, 0, 20, 200)
        wall9 = pygame.Rect(205, 0, 20, 540)
        wall10 = pygame.Rect(250, 0, 20, 200)
        wall11 = pygame.Rect(250, 230, 20, 375)
        wall12 = pygame.Rect(295, 0, 20, 540)
        wall13 = pygame.Rect(295, 0, 20, 200)
        wall14 = pygame.Rect(340, 230, 20, 375)
        wall15 = pygame.Rect(340, 0, 20, 200)
        wall16 = pygame.Rect(385, 0, 20, 540)
        wall17 = pygame.Rect(385, 0, 20, 200)
        wall18 = pygame.Rect(430, 230, 20, 375)
        wall19 = pygame.Rect(430, 0, 20, 200)
        wall20 = pygame.Rect(475, 0, 20, 540)
        wall21 = pygame.Rect(475, 0, 20, 200)

        # defining squares
        square1 = pygame.Rect(520, 50, 85, 85)
        square2 = pygame.Rect(520, 160, 85, 85)
        square3 = pygame.Rect(520, 270, 85, 85)
        square4 = pygame.Rect(520, 380, 85, 85)
        square5 = pygame.Rect(520, 490, 415, 85)
        square6 = pygame.Rect(630, 50, 85, 85)
        square7 = pygame.Rect(630, 160, 85, 85)
        square8 = pygame.Rect(630, 270, 85, 85)
        square9 = pygame.Rect(630, 380, 85, 85)
        square10 = pygame.Rect(630, 490, 85, 85)
        square11 = pygame.Rect(740, 50, 85, 85)
        square12 = pygame.Rect(740, 160, 85, 85)
        square13 = pygame.Rect(740, 270, 85, 85)
        square14 = pygame.Rect(740, 380, 85, 85)
        square15 = pygame.Rect(740, 490, 85, 85)
        square16 = pygame.Rect(850, 50, 85, 85)
        square17 = pygame.Rect(850, 160, 85, 85)
        square18 = pygame.Rect(850, 270, 85, 85)
        square19 = pygame.Rect(850, 380, 85, 85)
        square20 = pygame.Rect(850, 490, 85, 85)

        # defining winning square
        winning = pygame.Rect(940, 25, 65, 550)

        # defining borders
        bottom_border = pygame.Rect(0, 575, 1000, 25)
        top_border = pygame.Rect(0, 0, 1000, 25)

        # drawing winning square
        pygame.draw.rect(screen, green, winning)

        # drawing borders
        pygame.draw.rect(screen, red, bottom_border)
        pygame.draw.rect(screen, red, top_border)

        # drawing the wall part of maze
        pygame.draw.rect(screen, red, wall1)
        pygame.draw.rect(screen, red, wall2)
        pygame.draw.rect(screen, red, wall3)
        pygame.draw.rect(screen, red, wall4)
        pygame.draw.rect(screen, red, wall5)
        pygame.draw.rect(screen, red, wall6)
        pygame.draw.rect(screen, red, wall7)
        pygame.draw.rect(screen, red, wall8)
        pygame.draw.rect(screen, red, wall9)
        pygame.draw.rect(screen, red, wall10)
        pygame.draw.rect(screen, red, wall11)
        pygame.draw.rect(screen, red, wall12)
        pygame.draw.rect(screen, red, wall13)
        pygame.draw.rect(screen, red, wall14)
        pygame.draw.rect(screen, red, wall15)
        pygame.draw.rect(screen, red, wall16)
        pygame.draw.rect(screen, red, wall17)
        pygame.draw.rect(screen, red, wall18)
        pygame.draw.rect(screen, red, wall19)
        pygame.draw.rect(screen, red, wall20)
        pygame.draw.rect(screen, red, wall21)

        # drawing the square part of maze
        pygame.draw.rect(screen, red, square1)
        pygame.draw.rect(screen, red, square2)
        pygame.draw.rect(screen, red, square3)
        pygame.draw.rect(screen, red, square4)
        pygame.draw.rect(screen, red, square5)
        pygame.draw.rect(screen, red, square6)
        pygame.draw.rect(screen, red, square7)
        pygame.draw.rect(screen, red, square8)
        pygame.draw.rect(screen, red, square9)
        pygame.draw.rect(screen, red, square10)
        pygame.draw.rect(screen, red, square11)
        pygame.draw.rect(screen, red, square12)
        pygame.draw.rect(screen, red, square13)
        pygame.draw.rect(screen, red, square14)
        pygame.draw.rect(screen, red, square15)
        pygame.draw.rect(screen, red, square16)
        pygame.draw.rect(screen, red, square17)
        pygame.draw.rect(screen, red, square18)
        pygame.draw.rect(screen, red, square19)
        pygame.draw.rect(screen, red, square20)

        # if touching part of maze, dies, defines x as hacking variable
        # set x to any number but 1 to see what happens if you touch green
        x = 1
        if player_controlled.colliderect(bottom_border) and x == 1:
            player_x = 0
            player_y = 35
            pygame.display.update()
        elif player_controlled.colliderect(top_border) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall1) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall2) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall3) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall4) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall5) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall6) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall7) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall8) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall9) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall10) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall11) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall12) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall13) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall14) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall15) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall16) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall17) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall18) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall19) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall20) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(wall21) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square1) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square2) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square3) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square4) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square5) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square6) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square7) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square8) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square9) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square10) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square11) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square12) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square13) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square14) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square15) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square16) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square17) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square18) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square19) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square20) and x == 1:
            player_x = 0
            player_y = 35
        elif player_controlled.colliderect(square1) and x == 1:
            player_x = 0
            player_y = 35

        # if player reaches the end
        if player_controlled.colliderect(winning):
            screen.fill(black)
            ending = game_font.render("Congratulations on finishing! You win!", False, green)
            screen.blit(ending, (200, 250))

        # updates display
        pygame.display.update()
        screen.fill(black)


# difficulty selector
if difficulty == 1:
    main(0.75, 0, 35, 0, 0)
elif difficulty == 2:
    main(1.75, 0, 35, 0, 0)
elif difficulty == 3:
    main(2.75, 0, 35, 0, 0)
elif difficulty == 4:
    main(3.75, 0, 35, 0, 0)
elif difficulty not in [1, 2, 3, 4]:
    difficulty = eval(input("Choose a difficulty, the higher the number, the harder it is(1-4) "))
