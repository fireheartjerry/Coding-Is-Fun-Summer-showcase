# lesson 2
from random import randint # imports randint from random
while True: # infinite loop
    try_again = input("Would you like to try again? Press ENTER for yes and type E for no: ") #asks for try again
    lives = eval(input("How many turns do you want: "))
    if try_again == '': # if yes
        lower = eval(input("Enter your lower range: "))
        upper = eval(input("Enter your upper range: "))
        for i in range(lives): # lower and upper range
            if (upper - lower) < 5:
                lower = eval(input("Enter your lower range(your range is too low): "))
                upper = eval(input("Enter your upper range: "))
            answer = randint(lower,upper)
            guess = int(input(f"guess a number from {lower} to {upper}: "))
            if guess > answer:
                print("too small")
            elif guess < answer:
                print("too big")
            elif guess == answer:
                print("Correct!")
                print()
                break
        else:
            print("Wrong, you lost.")
            print()
            print(f"The number was {answer}")
    elif try_again == 'e' or try_again == 'E':
        print("You ended the program.")
        break
    else:
        try_again = input("You did not respond correctly. Would you like to try again? Press ENTER for yes and type E for no: ")