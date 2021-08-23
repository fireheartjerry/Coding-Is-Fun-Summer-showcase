from random import randint
answer = randint(1, 10)
guess = int(input("guess a number from 1 to 10: "))
if guess == answer:
    print("Correct!")
    print()
else:
    print("Wrong, you lost.")
    print()
    print("The number was",answer)