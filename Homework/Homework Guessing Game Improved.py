from random import randint 
# imports randint from random module
while True:
    difficulty = eval(input("Enter your difficulty, baby(1), easy(2), medium(3), hard(4), literally impossible(5): "))
    # asks for difficulty level

    hints = input("Would you like hints? [Y/N] ")
    # asks for hints
        
    if hints not in ["Y","y","N","n"]:
    # if entered nothing or wrong for hints
        hints = input("Do you want to play again? [Y/N] ")
        # asks again for hints yes no
        print()

    elif hints == "n" or hints == "N":
    # if hints entered no
        print("You are brave, we will not do hints.")
        # praises user and does no hints
        print()
        if difficulty == 1:
        # if difficulty is baby
            lives = 30
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 30
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 2:
        # if difficulty is easy
            lives = 20
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 20
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break
            

        elif difficulty == 3:
        # if difficulty is medium
            lives = 10
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 10
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 4:
        # if difficulty is hard
            lives = 5
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 5
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 5:
        # if difficulty is literally impossible
            lives = 3
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 3
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break

    elif hints == "y" or hints == "Y":
    # if hints entered yes
        print("Better safe than sorry! Ok we will do hints.")
        # "praises" user and does yes hints
        print()

        if difficulty == 1:
        # if difficulty is baby
            lives = 30
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 30
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 2:
        # if difficulty is easy
            lives = 20
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 20
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 3:
        # if difficulty is medium
            lives = 10
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 10
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    try_again = input("Do you want to play again? [Y/N] ")
                    print(f"The answer was {answer}")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 4:
        # if difficulty is hard
            lives = 5
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 5
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break



        elif difficulty == 5:
        # if difficulty is literally impossible
            lives = 3
            # sets lives
            lowerbound = eval(input("Enter your lowerbound range: "))
            # asks user for lowerbound range
            upperbound = eval(input("Enter your upperbound range: "))
            # asks user for upperbound range
            answer = randint(lowerbound,upperbound)
            # makes the answer a random number from lowerbound to upperound
            while True:
            # does a while loop that is forever unless typed break
                if upperbound - lowerbound <= 5:
                    # if the range is smaller or equal to 5
                    print("Your range was too low.")
                    # notifies user that range is too small
                    print()
                    lowerbound = eval(input("Enter your lowerbound range: "))
                    # asks again for lowerbound range
                    upperbound = eval(input("Enter your upperbound range: "))
                    # asks again for upperbound range
                print()
                guess = eval(input("Enter what you think the number is: "))
                # asks user for their guess
                print()

                if guess == answer:
                    # if user guesses correctly
                    print("Wow, you are so smart, you got it right!")
                    # praises user
                    print()
                    print()
                    break
                    # ends the loop

                else:
                    # if guess is no the answer
                    lives -= 1
                    # lives is subtracted by 1
                    print(f"You got it wrong, but, you can try again! \nYou have {lives} turns left.")
                    # prints that the user guessed it wrong, and the number of turns left
                    if hints == 'y' or hints == 'Y':
                        # if hints is true
                        if guess > answer:
                            print("For your next guess, try a lower guess!")
                            # prints lower if the guess is higher than the answer

                        elif guess < answer:
                            print("For your next guess, try a higher guess!")
                            # prints higher if the guess is lower than the answer

                        elif guess == answer:
                            print("You are smart, you got it right!")
                            # congratulates user if they get it right
                            break

                    elif hints == 'n' or hints == 'N':
                        # if hints is no
                        print()

                if lives == 0:
                    # if lives are 0
                    lives = 3
                    # resets lives
                    print(f"Uh oh! You still didnt get the answer after {lives} turns! And this was baby mode! You are not intelligent.")
                    print(f"The answer was {answer}")
                    try_again = input("Do you want to play again? [Y/N] ")
                    # asks user if they want to try again

                    if try_again not in ["Y","y","N","n"]:
                    # if user does not reply with yes or no
                        try_again = input("Do you want to play again? [Y/N] ")
                        # asks again

                    elif try_again == "n" or try_again == "N":
                    # if user responds with no
                        print("Ok! Thanks for playing!")
                        # thanks user for playing
                        print()
                        # leaves
                        exit()

                    elif try_again == "y" or try_again == "Y":
                        # if user responds with yes
                        print()
                        print()
                        # goes back to beginning
                    break

