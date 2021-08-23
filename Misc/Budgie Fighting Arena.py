#BUDGIE FIGHT!!
import time
from random import randint
Starting_Cash_1 = 100
Starting_Cash_2 = 100
Player_1_Wins = 0
Player_2_Wins = 0
Rounds = 0
def BudgieFight(HP_1,Attack_1,Defense_1,HP_2,Attack_2,Defense_2):
    global Starting_Cash_1
    global Starting_Cash_2
    global Player_1_Wins
    global Player_2_Wins
    global Rounds
    input("Welcome to the Budgie Fighting Arena! \nHere you can pit 2 birds together, with stats that you can choose.\nYou start with 100 HP, 10 Attack, and 1 Defense.\nMay the best(and luckiest) bird win!")
    print()
    while Rounds < 3:
        for i in range(1):
            print("\033[1;37mColours         \033[1;32mCOST   \033[1;31m ATTACK  \033[1;36m DEFENSE           ")
            print("\033[0;37mWhite           \033[1;32m$2.00   \033[1;31m   +6    \033[1;36m   +1   \033[0;37m(1)")
            print("\033[0;37mGrey            \033[1;32m$2.00   \033[1;31m   +4    \033[1;36m   +2   \033[0;37m(2)")
            print("\033[0;37mYellow          \033[1;32m$2.00   \033[1;31m   +8    \033[1;36m   +0   \033[0;37m(3)")
            print("\033[0;37mGreen           \033[1;32m$2.00   \033[1;31m   +3    \033[1;36m   +4   \033[0;37m(4)")
            print("\033[0;37mCyan            \033[1;32m$5.00   \033[1;31m   +6    \033[1;36m   +4   \033[0;37m(5)")
            print("\033[0;37mBlack           \033[1;32m$5.00   \033[1;31m   +8    \033[1;36m   +3   \033[0;37m(6)")
            print("\033[0;37mPurple          \033[1;32m$10.00  \033[1;31m   +10   \033[1;36m   +6   \033[0;37m(7)")
            print("\033[0;37mRed             \033[1;32m$10.00  \033[1;31m   +14   \033[1;36m   +3   \033[0;37m(8)")
            print("\033[0;37mMulti Colour    \033[1;32m$20.00  \033[1;31m   +16   \033[1;36m   +6   \033[0;37m(9)")
            print("\033[0;37mRainbow         \033[1;32m$30.00  \033[1;31m   +19   \033[1;36m   +9   \033[0;37m(10)")
            Buy_Colour = eval(input("\033[1;33mEnter Your Bird Colour Here: "))
            print()
            i = i
            if Buy_Colour == 1:
                Attack_1 = Attack_1+6
                Defense_1 = Defense_1+1
                Starting_Cash_1 = Starting_Cash_1-2
            elif Buy_Colour == 2:
                Attack_1 = Attack_1+4
                Defense_1 = Defense_1+2
                Starting_Cash_1 = Starting_Cash_1-2
            elif Buy_Colour == 3:
                Attack_1 = Attack_1+8
                Defense_1 = Defense_1+0
                Starting_Cash_1 = Starting_Cash_1-2
            elif Buy_Colour == 4:
                Attack_1 = Attack_1+3
                Defense_1 = Defense_1+4
                Starting_Cash_1 = Starting_Cash_1-2
            elif Buy_Colour == 5:
                Attack_1 = Attack_1+6
                Defense_1 = Defense_1+4
                Starting_Cash_1 = Starting_Cash_1-5
            elif Buy_Colour == 6:
                Attack_1 = Attack_1+8
                Defense_1 = Defense_1+3
                Starting_Cash_1 = Starting_Cash_1-5
            elif Buy_Colour == 7:
                Attack_1 = Attack_1+10
                Defense_1 = Defense_1+16
                Starting_Cash_1 = Starting_Cash_1-10
            elif Buy_Colour == 8:
                Attack_1 = Attack_1+14
                Defense_1 = Defense_1+3
                Starting_Cash_1 = Starting_Cash_1-10
            elif Buy_Colour == 9:
                Attack_1 = Attack_1+16
                Defense_1 = Defense_1+6
                Starting_Cash_1 = Starting_Cash_1-20
            elif Buy_Colour == 10:
                Attack_1 = Attack_1+19
                Defense_1 = Defense_1+9
                Starting_Cash_1 = Starting_Cash_1-30
            elif Buy_Colour == 1002:
                Attack_1 = Attack_1+1000
                Defense_1 = Defense_1+90
                HP_1 = 3*HP_1
            print("You now have",Starting_Cash_1,"Dollars left")
            print("\033[1;37mTraining             \033[1;32mCOST       \033[1;31mATTACK   \033[1;36mDEFENSE")
            print("\033[0;37mNo Pre-Training       \033[1;32m$0.00      \033[1;31m   +0    \033[1;36m   +0    \033[0;37m(1)")
            print("\033[0;37mPartial Training      \033[1;32m$10.00     \033[1;31m   +5    \033[1;36m   +5    \033[0;37m(2)")
            print("\033[0;37mRegular Training      \033[1;32m$20.00     \033[1;31m   +10   \033[1;36m   +10   \033[0;37m(3)")
            print("\033[0;37mAdvanced Training     \033[1;32m$35.00     \033[1;31m   +15   \033[1;36m   +15   \033[0;37m(4)")
            print("\033[0;37mExpert Training       \033[1;32m$50.00     \033[1;31m   +25   \033[1;36m   +25   \033[0;37m(5)")
            Buy_Train = eval(input("\033[1;33mEnter your option here: "))
            print()
            if Buy_Train == 1:
                Attack_1 = Attack_1+0
                Defense_1 = Defense_1+0
                Starting_Cash_1 = Starting_Cash_1-0
            elif Buy_Train == 2:
                Attack_1 = Attack_1+5
                Defense_1 = Defense_1+5
                Starting_Cash_1 = Starting_Cash_1-10
            elif Buy_Train == 3:
                Attack_1 = Attack_1+10
                Defense_1 = Defense_1+10
                Starting_Cash_1 = Starting_Cash_1-20
            elif Buy_Train == 4:
                Attack_1 = Attack_1+15
                Defense_1 = Defense_1+15
                Starting_Cash_1 = Starting_Cash_1-35
            elif Buy_Train == 5:
                Attack_1 = Attack_1+25
                Defense_1 = Defense_1+25
                Starting_Cash_1 = Starting_Cash_1-50
            print("You now have",Starting_Cash_1,"Dollars left")
            print("\033[1;37mBeaks                \033[1;32mCOST       \033[1;31mATTACK   \033[1;36mDEFENSE")
            print("\033[0;37mRegular Beak          \033[1;32m$0.00      \033[1;31m   +0    \033[1;36m   +0      \033[0;37m(1)")
            print("\033[0;37mStrong Beak           \033[1;32m$10.00     \033[1;31m   +3    \033[1;36m   +1      \033[0;37m(2)")
            print("\033[0;37mSharp Beak            \033[1;32m$20.00     \033[1;31m   +8    \033[1;36m   +1      \033[0;37m(3)")
            print("\033[0;37mRazer Sharp Beak      \033[1;32m$45.00     \033[1;31m   +13   \033[1;36m   +1      \033[0;37m(4)")
            print("\033[0;37mObsidian Beak         \033[1;32m$60.00     \033[1;31m   +19   \033[1;36m   +8      \033[0;37m(5)")
            print("\033[0;33mOBSIDIAN BEAK IS ALSO +15 HP")
            Buy_Beak = eval(input("\033[1;33mEnter your option here: "))
            print()
            if Buy_Beak == 1:
                Attack_1 = Attack_1+0
                Defense_1 = Defense_1+0
                Starting_Cash_1 = Starting_Cash_1-0
            elif Buy_Beak == 2:
                Attack_1 = Attack_1+3
                Defense_1 = Defense_1+1
                Starting_Cash_1 = Starting_Cash_1-10
            elif Buy_Beak == 3:
                Attack_1 = Attack_1+8
                Defense_1 = Defense_1+1
                Starting_Cash_1 = Starting_Cash_1-20
            elif Buy_Beak == 4:
                Starting_Cash_1 = Starting_Cash_1-45          
                if Starting_Cash_1 < 0:     
                    print("\033[1;31mError, you do not have enough money. As a punishment, we will be only adding 1 to attack and defense.")
                    print()
                    Attack_1 = Attack_1+1
                    Defense_1 = Defense_1+1
                elif Starting_Cash_1 > 0:
                    Attack_1 = Attack_1+13
                    Defense_1 = Defense_1+1
            elif Buy_Beak == 5:
                Starting_Cash_1 = Starting_Cash_1-60
                if Starting_Cash_1 < 0:
                    print("\033[1;31mError, you do not have enough money. As a punishment, we will be only adding 1 to attack and defense.")
                    print()
                    Attack_1 = Attack_1+1
                    Defense_1 = Defense_1+1
                elif Starting_Cash_1 > 0:
                    Attack_1 = Attack_1+19
                    Defense_1 = Defense_1+8
                    HP_1 = HP_1+15
            if Starting_Cash_1 < 0:
                Starting_Cash_1 = 0
            print("You now have",Starting_Cash_1,"Dollars left, your left-over money will be converted into HP points.")
            HP_1 = HP_1+Starting_Cash_1
            print()
            time.sleep(1)
            print("\033[1;37mProcessing Information...")
            time.sleep(3)
            print("\033[1;37mPlayer 1 is complete!")
            time.sleep(3)
            input("\033[1;37mPlayer 2, press ENTER to begin your bird.")
            print("\n"*10)
            for i in range(1):
                print("\033[1;37mColours         \033[1;32mCOST   \033[1;31m ATTACK  \033[1;36m DEFENSE           ")
                print("\033[0;37mWhite           \033[1;32m$2.00   \033[1;31m   +6    \033[1;36m   +1   \033[0;37m(1)")
                print("\033[0;37mGrey            \033[1;32m$2.00   \033[1;31m   +4    \033[1;36m   +2   \033[0;37m(2)")
                print("\033[0;37mYellow          \033[1;32m$2.00   \033[1;31m   +8    \033[1;36m   +0   \033[0;37m(3)")
                print("\033[0;37mGreen           \033[1;32m$2.00   \033[1;31m   +3    \033[1;36m   +4   \033[0;37m(4)")
                print("\033[0;37mCyan            \033[1;32m$5.00   \033[1;31m   +6    \033[1;36m   +4   \033[0;37m(5)")
                print("\033[0;37mBlack           \033[1;32m$5.00   \033[1;31m   +8    \033[1;36m   +3   \033[0;37m(6)")
                print("\033[0;37mPurple          \033[1;32m$10.00  \033[1;31m   +10   \033[1;36m   +6   \033[0;37m(7)")
                print("\033[0;37mRed             \033[1;32m$10.00  \033[1;31m   +14   \033[1;36m   +3   \033[0;37m(8)")
                print("\033[0;37mMulti Colour    \033[1;32m$20.00  \033[1;31m   +16   \033[1;36m   +6   \033[0;37m(9)")
                print("\033[0;37mRainbow         \033[1;32m$30.00  \033[1;31m   +19   \033[1;36m   +9   \033[0;37m(10)")
                Buy_Colour = eval(input("\033[1;33mEnter Your Bird Colour Here: "))
                print()
                i = i
                if Buy_Colour == 1:
                    Attack_2 = Attack_2+6
                    Defense_2 = Defense_2+1
                    Starting_Cash_2 = Starting_Cash_2-2
                elif Buy_Colour == 2:
                    Attack_2 = Attack_2+4
                    Defense_2 = Defense_2+2
                    Starting_Cash_2 = Starting_Cash_2-2
                elif Buy_Colour == 3:
                    Attack_2 = Attack_2+8
                    Defense_2 = Defense_2+0
                    Starting_Cash_2 = Starting_Cash_2-2
                elif Buy_Colour == 4:
                    Attack_2 = Attack_2+3
                    Defense_2 = Defense_2+4
                    Starting_Cash_2 = Starting_Cash_2-2
                elif Buy_Colour == 5:
                    Attack_2 = Attack_2+6
                    Defense_2 = Defense_2+4
                    Starting_Cash_2 = Starting_Cash_2-5
                elif Buy_Colour == 6:
                    Attack_2 = Attack_2+8
                    Defense_2 = Defense_2+3
                    Starting_Cash_2 = Starting_Cash_2-5
                elif Buy_Colour == 7:
                    Attack_2 = Attack_2+10
                    Defense_2 = Defense_2+16
                    Starting_Cash_2 = Starting_Cash_2-10
                elif Buy_Colour == 8:
                    Attack_2 = Attack_1+14
                    Defense_2 = Defense_2+3
                    Starting_Cash_2 = Starting_Cash_2-10
                elif Buy_Colour == 9:
                    Attack_2 = Attack_2+16
                    Defense_2 = Defense_2+6
                    Starting_Cash_2 = Starting_Cash_2-20
                elif Buy_Colour == 10:
                    Attack_2 = Attack_2+19
                    Defense_2 = Defense_2+9
                    Starting_Cash_2 = Starting_Cash_2-30
                elif Buy_Colour == 1002:
                    Attack_2 = Attack_2+1000
                    Defense_2 = Defense_2+90
                    HP_2 = 3*HP_2
                print("You now have",Starting_Cash_2,"Dollars left")
                print("\033[1;37mTraining             \033[1;32mCOST       \033[1;31mATTACK   \033[1;36mDEFENSE")
                print("\033[0;37mNo Pre-Training       \033[1;32m$0.00      \033[1;31m   +0    \033[1;36m   +0    \033[0;37m(1)")
                print("\033[0;37mPartial Training      \033[1;32m$10.00     \033[1;31m   +5    \033[1;36m   +5    \033[0;37m(2)")
                print("\033[0;37mRegular Training      \033[1;32m$20.00     \033[1;31m   +10   \033[1;36m   +10   \033[0;37m(3)")
                print("\033[0;37mAdvanced Training     \033[1;32m$35.00     \033[1;31m   +15   \033[1;36m   +15   \033[0;37m(4)")
                print("\033[0;37mExpert Training       \033[1;32m$50.00     \033[1;31m   +25   \033[1;36m   +25   \033[0;37m(5)")
                Buy_Train = eval(input("\033[1;33mEnter your option here: "))
                print()
                if Buy_Train == 1:
                    Attack_2 = Attack_2+0
                    Defense_2 = Defense_2+0
                    Starting_Cash_2 = Starting_Cash_2-0
                elif Buy_Train == 2:
                    Attack_2 = Attack_2+5
                    Defense_2 = Defense_2+5
                    Starting_Cash_2 = Starting_Cash_2-10
                elif Buy_Train == 3:
                    Attack_2 = Attack_2+10
                    Defense_2 = Defense_2+10
                    Starting_Cash_2 = Starting_Cash_2-20
                elif Buy_Train == 4:
                    Attack_2 = Attack_2+15
                    Defense_2 = Defense_2+15
                    Starting_Cash_2 = Starting_Cash_2-35
                elif Buy_Train == 5:
                    Attack_2 = Attack_2+25
                    Defense_2 = Defense_2+25
                    Starting_Cash_2 = Starting_Cash_2-50
                print("You now have",Starting_Cash_2,"Dollars left")
                print("\033[1;37mBeaks                \033[1;32mCOST       \033[1;31mATTACK   \033[1;36mDEFENSE")
                print("\033[0;37mRegular Beak          \033[1;32m$0.00      \033[1;31m   +0    \033[1;36m   +0      \033[0;37m(1)")
                print("\033[0;37mStrong Beak           \033[1;32m$10.00     \033[1;31m   +3    \033[1;36m   +1      \033[0;37m(2)")
                print("\033[0;37mSharp Beak            \033[1;32m$20.00     \033[1;31m   +8    \033[1;36m   +1      \033[0;37m(3)")
                print("\033[0;37mRazer Sharp Beak      \033[1;32m$45.00     \033[1;31m   +13   \033[1;36m   +1      \033[0;37m(4)")
                print("\033[0;37mObsidian Beak         \033[1;32m$60.00     \033[1;31m   +19   \033[1;36m   +8      \033[0;37m(5)")
                print("\033[0;33mOBSIDIAN BEAK IS ALSO +15 HP")
                Buy_Beak = eval(input("\033[1;33mEnter your option here: "))
                print()
                if Buy_Beak == 1:
                    Attack_2 = Attack_2+0
                    Defense_2 = Defense_2+0
                    Starting_Cash_2 = Starting_Cash_2-0
                elif Buy_Beak == 2:
                    Attack_2 = Attack_2+3
                    Defense_2 = Defense_2+1
                    Starting_Cash_2 = Starting_Cash_2-10
                elif Buy_Beak == 3:
                    Attack_2 = Attack_2+8
                    Defense_2 = Defense_2+1
                    Starting_Cash_2 = Starting_Cash_2-20
                elif Buy_Beak == 4:
                    Starting_Cash_2 = Starting_Cash_2-45          
                    if Starting_Cash_1 < 0:     
                        print("\033[1;31mError, you do not have enough money. As a punishment, we will be only adding 1 to attack and defense.")
                        print()
                        Attack_2 = Attack_2+1
                        Defense_2 = Defense_2+1
                    elif Starting_Cash_1 > 0:
                        Attack_2 = Attack_2+15
                        Defense_2 = Defense_2+15
                elif Buy_Beak == 5:
                    Starting_Cash_2 = Starting_Cash_2-60
                    if Starting_Cash_1 < 0:
                        print("\033[1;31mError, you do not have enough money. As a punishment, we will be only adding 1 to attack and defense.")
                        print()
                        Attack_2 = Attack_2+1
                        Defense_2 = Defense_2+1
                    elif Starting_Cash_1 > 0:
                        Attack_2 = Attack_2+19
                        Defense_2 = Defense_2+8
                        HP_2 = HP_2+15
                if Starting_Cash_2 < 0:
                    Starting_Cash_2 = 0        
                print("You now have",Starting_Cash_2,"Dollars left, your left-over money will be converted into HP points.")    
                HP_2 = HP_2+Starting_Cash_2
                print()
                time.sleep(1)
                print("\033[1;37mProcessing Information...")
                time.sleep(3)
                print("\033[1;37mPlayer 2 is complete!")
                time.sleep(3)
                print("\033[1;37mPlayer 1 Stats\nAttack:\033[1;31m",Attack_1,"\n\033[1;37mDefense:\033[1;36m",Defense_1,"\n\033[1;37mHP:\033[1;32m",HP_1)
                print()
                print()
                print("\033[1;37mPlayer 2 Stats\nAttack:\033[1;31m",Attack_2,"\n\033[1;37mDefense:\033[1;36m",Defense_2,"\n\033[1;37mHP:\033[1;32m",HP_2)
                input("\033[1;37mPlayer 1, press ENTER to confirm you are here: ")
                input("\033[1;37mPlayer 2, press ENTER to confirm you are here: ")
                while True:
                    HP_1 = abs(HP_1)
                    HP_2 = abs(HP_2)
                    if Defense_1 >= 100:
                        Defense_1 = 99
                    elif Defense_2 >= 100:
                        Defense_2 = 99
                    input("\033[1;37mPlayer 1, press ENTER to attack! ")
                    Attack_base_1 = randint(10,50)
                    print("\033[1;37mYour attack base is",Attack_base_1)
                    time.sleep(1.5)
                    player1_attack_percentage = 100 - Attack_1
                    player2_attack_percentage = 100 - Attack_2
                    player1_defense_percentage = 100 - Defense_1
                    player2_defense_percentage = 100 - Defense_2
                    player1_total_attack_percentage = (player1_attack_percentage*player2_defense_percentage)/10000
                    player2_total_attack_percentage = (player2_attack_percentage*player1_defense_percentage)/10000
                    player2_total_attack_percentage = abs(player2_total_attack_percentage)
                    player1_total_attack_percentage = abs(player2_total_attack_percentage)
                    print("\033[1;37mSince your damage output is",Attack_1,"and your opponent's defense is",Defense_2,"\nYou deal your attacks percent multiplied by your opponents defense percent multiplied by the attack base. \nYou deal\033[1;31m",round(player1_total_attack_percentage*Attack_base_1),"\033[0;37mDamage")
                    HP_2 = HP_2 - round(abs(player1_total_attack_percentage*Attack_base_1))
                    print("\033[1;37mPlayer 2 has\033[1;32m",HP_2,"\033[1;37mhealth.")
                    input("\033[1;37mPlayer 2, press ENTER to attack! ")
                    Attack_base_2 = randint(10,50)
                    print("\033[1;37mYour attack base is",Attack_base_2)
                    time.sleep(3)
                    print("\033[1;37mSince your damage output is",Attack_1,"and your opponent's defense is",Defense_2,"\nYou deal your attacks percent multiplied by your opponents defense percent multiplied by the attack base. \nYou deal\033[1;31m",round(player2_total_attack_percentage*Attack_base_2),"\033[0;37mDamage")
                    HP_1 = HP_1 - round(abs(player2_total_attack_percentage*Attack_base_2))
                    print("\033[1;37mPlayer 1 has\033[1;32m",HP_1,"\033[1;37mhealth.")
                    if HP_1 <= 0:
                        input("\033[1;37mPlayer 1, this will be your final attack before you die! Press ENTER for your final hit! ")
                        Attack_base_death_1 = randint(10,35)
                        print("\033[1;37mSince your damage output is",Attack_1,"and your opponent's defense is",Defense_2,"\nYou deal your attacks percent multiplied by your opponents defense percent multiplied by the attack base. \nYou deal\033[1;31m",round(player1_total_attack_percentage*Attack_base_death_1),"\033[0;37mDamage")
                        if HP_2 <= 0:
                            print("\033[1;37mUH OH Player 1 landed a Game-Ending hit on Player 2, and they are both dead. TIE")
                            print()
                            Player_1_Wins = Player_1_Wins+1
                            Player_2_Wins = Player_2_Wins+1
                            Rounds = Rounds+1
                            break
                        else:
                            print("\033[1;37mPlayer 1 tried his best, but he could not defeat Player 2, Player 2 wins!")
                            print()
                            Player_2_Wins = Player_2_Wins+1
                            Rounds = Rounds+1
                            break
                    elif HP_2 <= 0:
                        input("\033[1;37mPlayer 2, this will be your final attack before you die! Press ENTER for your final hit! ")
                        Attack_base_death_2 = randint(10,35)
                        print("\033[1;37mSince your damage output is",Attack_1,"and your opponent's defense is",Defense_2,"\nYou deal your attacks percent multiplied by your opponents defense percent multiplied by the attack base. \nYou deal\033[1;31m",player2_total_attack_percentage*Attack_base_death_2,"\033[0;37mDamage")
                        if HP_1 <= 0:
                            print("\033[1;37mUH OH Player 1 landed a Game-Ending hit on Player 2, and they are both dead. TIE")
                            print()
                            Player_1_Wins = Player_1_Wins+1
                            Player_2_Wins = Player_2_Wins+1
                            Rounds = Rounds+1
                            break
                        else:
                            print("Player 2 tried their best, but they could not defeat Player 1, Player 1 wins!")
                            print()
                            Player_1_Wins = Player_1_Wins+1
                            Rounds = Rounds+1
                            break
                    print()                                                       
BudgieFight(100,10,1,100,10,1)
