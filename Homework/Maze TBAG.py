def TrappedInPocketDimension():
    choice_list = ["Would you go left or right(L/R) "]
    HP = 7
    PTSD = 0
    Human = 100
    print("You are trapped in a pocket dimension, you must travel through a maze to escape.\nYour current stats are:\nHP: 10\nPTSD: 0\nHuman: 100%\nYour goal is to make it out alive with below 5 PTSD\nAt least 85% of your body human\nAnd HP above 0\n")
    hi = input("Press ENTER to continue: ")
    print(hi)
    for i in range(5):
        question = str(choice_list[i])
        question = question.replace("[","")
        question = question.replace("]","")
        question = question.replace(",","")
        question = question.replace("'","")
        ask = input(question)
        print()
        ask = ask.upper
        if i == 0 and ask == "R":
            print("You turn a corner to find...nothing.\nYou breathe a sigh of relief, and keep moving.")
        elif i == 0 and ask != "R":
            print("You turn a corner to find a mutant spider, It sinks its fangs into your body and poisons your arm.\nThen it leaves and you crawl onwards.\nYou lose 2 HP, 5% human, and gain 3 PTSD.")
            HP -= 2
            Human -= 5
            PTSD += 3
        elif i == 1 and ask == "R":
            print("You walk onwards and fall into a hole in the ground\nThere, you see a sleeping dragon, you cautiosly tiptoe away...")
        elif i == 1 and ask != "R":
            print("You walk onwards and fall into a hole in the ground\nYou land on a sleeping dragon, which awakes and immediately attacks\nYou fend it off, but not without injuries.\nYou lose 5% of human, gain 1 PTSD, and lose 3 HP.")
            HP -= 3
            Human -= 5
            PTSD += 1
        elif i == 2 and ask == "L":
            print("You slash your way accross some tangled vines and find many carnivorous plants,\nYou have a grappling hook, and swing away.")
        elif i == 2 and ask != "L":
            print("You slash your way accross some tangled vines\nHowever, you trip on one and fall into the gaping mouth of a giant carnivorous plant.\nYou manage to slice your way through,\nBut you lose 7% human, gain 2 PTSD, and lose 2 HP.")
            HP -= 2
            Human -= 7
            PTSD += 2
        elif i == 3 and ask == "R":
            print("You find a box and break it open, inside is a flamethrower\nJust that second, hundreds of hornets swarm you, luckily, you kill them with the flamethrower.")
        elif i == 3 and ask != "R":
            print("You find a box and break it open, inside is a note saying \"run when you can, quickly!\"\nThen, hundreds of hornets swarm you, stinging you and flying away.\nYou lose 6% human, lose 3 HP, and gain 2 PTSD.")
            HP -= 3
            Human -= 6
            PTSD += 2
        elif i == 4 and ask == "L":
            print("You meet a giant dark blob that has several black tentacles\nYou run as fast as you can and crash straight into a wall\nLuckily for you, the wall is actually a reality portal and you get zapped back into earth.")
            if PTSD >= 5:
                print("You have too much PTSD and lose.")
                exit()
            if HP <= 0:
                print("You succumbed to your injuries.")
                exit()
            if Human <= 90:
                print("Other humans think you are a monster and you die.")
                exit()
        elif i == 4 and ask != "L":
            print("You see a giant dark blob that has several black tentacles\nYou run as fast as you can and crash straight into a wall\nIt gets you.")
            exit()
TrappedInPocketDimension()



