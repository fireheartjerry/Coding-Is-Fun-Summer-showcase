def TrappedInPocketDimension():
    attempts = input("Enter how many games you want: ")
    if int(attempts) <= 0:
        print("\033[1;31mInvalid input, try again.")
        attempts = input("\033[0;37mEnter how many games you want: ")
    elif attempts == '':
        attempts = 1
    for i in range(int(attempts)):
        Answer_key = ["R","R","L","R","R"]
        Player_Answer_Log = []
        HP = 7
        PTSD = 0
        Human = 100
        print("\033[1;36mYou are trapped in a pocket dimension, you must travel through a maze to escape.\nYour current stats are:\nHP: 10\nPTSD: 0\nHuman: 100%\nYour goal is to make it out alive with below 5 PTSD\nAt least 85% of your body human\nAnd HP above 0\n")
        for i in range(5):
            i = i
            ask = input("\033[1;37mLeft or Right[L/R]")
            Player_Answer_Log.append(ask)
            print()
            ask = ask.upper()
            if ask == "R":
                print("\033[1;32mYou turn a corner to find...nothing.\nYou breathe a sigh of relief, and keep moving.")
            elif ask != "R":
                print("\033[1;31mYou turn a corner to find a mutant spider, It sinks its fangs into your body and poisons your arm.\nThen it leaves and you crawl onwards.\n\033[1;37mYou lose 2 HP, 5% human, and gain 3 PTSD.")
                HP -= 2
                Human -= 5
                PTSD += 3
                print("Your stats are:\n\033[1;31mHP:",HP,"\033[1;32m\nHuman:",Human,"%\033[1;33m\nPTSD:",PTSD)
                if PTSD >= 5:
                    print("\033[1;31mYou have too much PTSD and waste all your money on therapy.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if HP <= 0:
                    print("\033[1;31mYou succumbed to your injuries.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if Human <= 85:
                    print("\033[1;31mOther humans think you are a monster and you die.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
            print()
            ASK = input("\033[1;37mLeft or Right[L/R]")
            Player_Answer_Log.append(ASK)
            print()
            ASK = ASK.upper()
            if ASK == "R":
                print("\033[1;32mYou walk onwards and fall into a hole in the ground\nThere, you see a sleeping dragon, you cautiosly tiptoe away...")
            elif ASK != "R":
                print("\033[1;31mYou walk onwards and fall into a hole in the ground\nYou land on a sleeping dragon, which awakes and immediately attacks\nYou fend it off, but not without injuries.\n\033[1;37mYou lose 5% of human, gain 1 PTSD, and lose 3 HP.")
                HP -= 3
                Human -= 5
                PTSD += 1
                print("\033[1;37mYour stats are:\n\033[1;31mHP:",HP,"\n\033[1;32mHuman:",Human,"%\n\033[1;33mPTSD:",PTSD)
                if PTSD >= 5:
                    print("\033[1;31mYou have too much PTSD and waste all your money on therapy.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if HP <= 0:
                    print("\033[1;31mYou succumbed to your injuries.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if Human <= 85:
                    print("\033[1;31mOther humans think you are a monster and you die.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
            print()
            AsK = input("\033[1;37mLeft or Right[L/R]")
            Player_Answer_Log.append(AsK)
            print()
            AsK = AsK.upper()
            if AsK == "L":
                print("\033[1;32mYou slash your way accross some tangled vines and find many carnivorous plants,\nYou have a grappling hook, and swing away.\n")
            elif AsK != "L":
                print("\033[1;31mYou slash your way accross some tangled vines\nHowever, you trip on one and fall into the gaping mouth of a giant carnivorous plant.\nYou manage to slice your way through,\n\033[1;37mBut you lose 7% human, gain 2 PTSD, and lose 2 HP.\n")
                HP -= 2
                Human -= 7
                if PTSD >= 5:
                    print("\033[1;31mYou have too much PTSD and waste all your money on therapy.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if HP <= 0:
                    print("\033[1;31mYou succumbed to your injuries.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if Human <= 85:
                    print("\033[1;31mOther humans think you are a monster and you die.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
            aSk = input("\033[1;37mLeft or Right[L/R]")
            Player_Answer_Log.append(aSk)
            print()
            aSk = aSk.upper()
            if aSk == "R":
                print("\033[1;32mYou find a box and break it open, inside is a flamethrower\nJust that second, hundreds of hornets swarm you, luckily, you kill them with the flamethrower.")
            elif aSk != "R":
                print("\033[1;31mYou find a box and break it open, inside is a note saying \"run when you can, quickly!\"\nThen, hundreds of hornets swarm you, stinging you and flying away.\n\033[1;37mYou lose 6% human, lose 3 HP, and gain 2 PTSD.")
                HP -= 3
                Human -= 6
                PTSD += 2
                print("Your stats are:\n\033[1;31mHP:",HP,"\033[1;32m\nHuman:",Human,"%\033[1;33m\nPTSD:",PTSD)
                if PTSD >= 5:
                    print("\033[1;31mYou have too much PTSD and waste all your money on therapy.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if HP <= 0:
                    print("\033[1;31mYou succumbed to your injuries.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if Human <= 85:
                    print("\033[1;31mOther humans think you are a monster and you die.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
            print()
            aSK = input("\033[1;37mLeft or Right[L/R]")
            Player_Answer_Log.append(aSK)
            print()
            aSK = aSK.upper()
            if aSK == "L":
                print("\033[1;32mYou meet a giant dark blob that has several black tentacles\nYou run as fast as you can and crash straight into a wall\nLuckily for you, the wall is actually a reality portal and you get zapped back into earth.")
                print("Your stats are:\n\033[1;31mHP:",HP,"\033[1;32m\nHuman:",Human,"%\033[1;33m\nPTSD:",PTSD)
                if PTSD >= 5:
                    print("\033[1;31mYou have too much PTSD and waste all your money on therapy.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if HP <= 0:
                    print("\033[1;31mYou succumbed to your injuries.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                if Human <= 85:
                    print("\033[1;31mOther humans think you are a monster and you die.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
                else:
                    print("\033[1;32mCongratulations, you survived the pocket dimension with some injuries, but you manage to have a \"normal\" life.")
                    print("Your answers were:",Player_Answer_Log)
                    print()
                    if attempts == 1:
                        exit()
            elif aSK != "L":
                print("\033[0;31mYou see a giant dark blob that has several black tentacles\nYou run as fast as you can and crash straight into a wall\n\033[1;31mIt gets you...")
                print("You lose.\033[0;37m")
                print("Your answers were:",Player_Answer_Log)
                if attempts == 1:
                    exit()
                else:
                    print("Next game:\n")
    print("The correct answers were:",Answer_key)
TrappedInPocketDimension()