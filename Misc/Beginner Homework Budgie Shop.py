'''Beginner Homework'''
def BudgieShop():
    from random import randint
    import time
    input("\033[1;36mPress Enter to continue. ")
    print()
    input("\033[1;36mWelcome to Jerry's Budgie SuperStore! ")
    input("We have many varieties of Budgies. ")
    input("They are affordable and fun. ")
    input("Take your picking of any bird here! Many colours, pre-trained, and special types! ")
    input("BUDGIES ARE YOUR BEST FREIND!!!!")
    print()
    print("\033[1;37m==================\nP r i c e  L i s t\n==================\033[1;37m\nBudgie Base Cost: \033[1;32m$20.00\033[0;37m\n")
    print()
    print("\033[1;37mCOLOURS ADD-ONS\n\033[0;37mWhite = \033[1;32m+$0.00\n\033[0;37mGrey = \033[1;32m+$0.00\n\033[0;37mGreen = \033[1;32m+$0.00\n\033[0;37mYellow = \033[1;32m+$0.00\n\033[0;37mCyan = \033[1;32m+$4.99\n\033[0;37mBlack = \033[1;32m+$4.99\n\033[0;37mPurple = \033[1;32m+$9.99\n\033[0;37mRed = \033[1;32m+$9.99\n\033[0;37mMulti-Colour Type 1 = \033[1;32m+$19.99\n\033[0;37mMulti-Colour Type 2 = \033[1;32m+$19.99\n\033[0;37mMulti-Colour Type 3 = \033[1;32m+$19.99\n\033[0;37mRainbow = \033[1;32m+$29.99\n")
    print()
    print("\033[1;37mTRAINING ADD-ONS\n\033[0;37mNo Pre-training = \033[1;32m+$0.00\n\033[0;37mPartial Training(Not afraid of Humans, Stands on hand, Potty Trained) = \033[1;32m+$14.99\n\033[0;37mRegular Training(At ease with Humans, Loyal to new owners, Can grab, Can bring outside) = \033[1;32m+$29.99\n\033[0;37mAdvanced Training(Completely happy with Humans, Trusting, Basic Talking) = \033[1;32m+$49.99\n\033[0;37mExpert Training(Can do tricks, Advanced voice mimicking skills, Professional Training) = \033[1;32m+$69.99\n")
    print()
    print("\033[1;37mSPECIAL BUDGIE ADD-ONS\n\033[0;37mNone = \033[1;32m+$0.00\n\033[0;37mGlow In the Dark = \033[1;32m+$399.99\n\033[0;37mExtra Strong = \033[1;32m+$499.99\n\033[0;37mEagle-Sight = \033[1;32m+$299.99\n\033[0;37mExtra Big = \033[1;32m+$99.99\n\033[0;37mRobot Budgie = \033[1;32m+$5999.99\n")
    print()
    print("\033[1;37mSERVICES\n\033[0;37mCheck-up + wash = \033[1;32m$19.99\n\033[0;37mNail Trim = \033[1;32m$9.99\n\033[0;37mWing Trim = \033[1;32m$9.99\n\033[0;37mFull Bird Wash= \033[1;32m$9.99\n\033[0;37m1 Year Unlimited Pass \033[1;32m+$199.99\n\033[0;37mLifetime Unlimited Pass \033[1;32m+$999.99\n")
    print()
    print("\033[1;37mOTHERS\n\033[0;37mRegular Cage = \033[1;32m$79.99\n\033[0;37mLarge Cage = \033[1;32m$99.99\n\033[0;37mRegular Food = \033[1;32m$19.99\n\033[0;37mPremium Food = \033[1;32m$29.99\n\033[0;37mCage Pack = \033[1;32m$19.99\n\033[0;37mFish Bones(1 bag) = \033[1;32m$4.99\n")    
    input()
    Item_list = []
    Price_list = []
    Base = 20
    while True:
        for i in range(1):
            print("\033[0;37mBudgie base cost is $20.00")
            print("\033[1;37mColours\n")
            print("\033[0;37mWhite           \033[1;32m+$0.00   \033[0;37m(1)")
            print("\033[0;37mGrey            \033[1;32m+$0.00   \033[0;37m(2)")
            print("\033[0;37mYellow          \033[1;32m+$0.00   \033[0;37m(3)")
            print("\033[0;37mGreen           \033[1;32m+$0.00   \033[0;37m(4)")
            print("\033[0;37mCyan            \033[1;32m+$4.99   \033[0;37m(5)")
            print("\033[0;37mBlack           \033[1;32m+$4.99   \033[0;37m(6)")
            print("\033[0;37mPurple          \033[1;32m+$9.99   \033[0;37m(7)")
            print("\033[0;37mRed             \033[1;32m+$9.99   \033[0;37m(8)")
            print("\033[0;37mMulti Colour 1  \033[1;32m+$19.99  \033[0;37m(9)")
            print("\033[0;37mMulti Colour 2  \033[1;32m+$19.99  \033[0;37m(10)")
            print("\033[0;37mMulti COlour 3  \033[1;32m+$19.99  \033[0;37m(11)")
            print("\033[0;37mRainbow         \033[1;32m+$29.99  \033[0;37m(12)")
            Buy_Colour = eval(input("\033[1;33mEnter Your budgie Colour Here: "))
            print()
            if Buy_Colour == 1:
                Item_list.append("White")
                Price_list.append(0)
            elif Buy_Colour == 2:
                Item_list.append("Grey")
                Price_list.append(0)
            elif Buy_Colour == 3:
                Item_list.append("Yellow")
                Price_list.append(3)
            elif Buy_Colour == 4:
                Item_list.append("Green")
                Price_list.append(0)
            elif Buy_Colour == 5:
                Item_list.append("Cyan")
                Price_list.append(5)
            elif Buy_Colour == 6:
                Item_list.append("Black")
                Price_list.append(5)
            elif Buy_Colour == 7:
                Item_list.append("Purple")
                Price_list.append(10)
            elif Buy_Colour == 8:
                Item_list.append("Red")
                Price_list.append(10)
            elif Buy_Colour == 9:
                Item_list.append("Multi colour 1")
                Price_list.append(20)
            elif Buy_Colour == 10:
                Item_list.append("Multi colour 2")
                Price_list.append(20)
            elif Buy_Colour == 11:
                Item_list.append("Multi colour 3")
                Price_list.append(20)
            elif Buy_Colour == 12:
                Item_list.append("Rainbow")
                Price_list.append(30)
            print("\n")
        for i in range(1):
            print("\033[1;37mTraining Add-Ons")
            print("\033[0;37mNo Pre-Training   \033[1;32m+$0.00        \033[0;37m(1)")
            print("\033[0;37mPartial Training   \033[1;32m+$14.99      \033[0;37m(2)")
            print("\033[0;37mRegular Training   \033[1;32m+$29.99      \033[0;37m(3)")
            print("\033[0;37mAdvanced Training  \033[1;32m+$49.99      \033[0;37m(4)")
            print("\033[0;37mExpert Training    \033[1;32m+$69.99      \033[0;37m(5)")
            Buy_Train = eval(input("\033[1;33mEnter your option here: "))
            print("\n")
            if Buy_Train == 1:
                Item_list.append("None")
                Price_list.append(0)
            elif Buy_Train == 2:
                Item_list.append("Partial")
                Price_list.append(15)
            elif Buy_Train == 3:
                Item_list.append("Regular")
                Price_list.append(30)
            elif Buy_Train == 4:
                Item_list.append("Advanced")
                Price_list.append(50)
            elif Buy_Train == 5:
                Item_list.append("Expert")
                Price_list.append(70)
        for i in range(1):
            print("\033[1;37mSpecial Add-Ons")
            print("\033[0;37mGlow In the Dark   \033[1;32m+$399.99    \033[0;37m(1)")
            print("\033[0;37mExtra Strong       \033[1;32m+$499.99    \033[0;37m(2)")
            print("\033[0;37mEagle Sight        \033[1;32m+$299.99    \033[0;37m(3)")
            print("\033[0;37mExtra Big          \033[1;32m+$99.99     \033[0;37m(4)")
            print("\033[0;37mRobot Budgie       \033[1;32m+$5999.99   \033[0;37m(5)")
            print("\033[0;37mNone               \033[1;32m+$0.00      \033[0;37m(6)")
            Buy_Special = eval(input("\033[1;33mEnter your option here: "))
            print()
            if Buy_Special == 1:
                Item_list.append("Glow In the Dark")
                Price_list.append(400)
            elif Buy_Special == 2:
                Item_list.append("Extra Strong")
                Price_list.append(500)
            elif Buy_Special == 3:
                Item_list.append("Eagle Sight")
                Price_list.append(300)
            elif Buy_Special == 4:
                Item_list.append("Extra Big")
                Price_list.append(100)
            elif Buy_Special == 5:
                Item_list.append("Robot Budgie")
                Price_list.append(6000)
            elif Buy_Special == 6:
                Item_list.append("None")
                Price_list.append(0)
        for i in range(1):
            print("\033[1;37mServices")
            print("\033[0;37mNone                       \033[1;32m+$0.00       \033[0;37m(1)")
            print("\033[0;37m1 Year Unlimited Pass      \033[1;32m+$199.99      \033[0;37m(2)")
            print("\033[0;37mLifetime Unlimited Pass    \033[1;32m+$999.99      \033[0;37m(3)")
            Buy_services = eval(input("\033[1;33mEnter your option here: "))
            print()
            if Buy_services == 1:
                Item_list.append("None")
                Price_list.append(0)
            elif Buy_services == 2:
                Item_list.append("1 Year Pass")
                Price_list.append(200)
            elif Buy_services == 3:
                Item_list.append("Lifetime Pass")
                Price_list.append(1000)
        for i in range(1):
            cage = eval(input("\033[0;37mWould you like a Regular(1), Large(2), or No(3) cage? Cost: \033[1;32m+$79.99 \033[0;37mRegular, \033[1;32m+$99.99 \033[0;37mLarge "))
            food = eval(input("\033[0;37mWould you like Regular(1), Premium(2), or No(3) food? Cost: \033[1;32m+$19.99 \033[0;37mRegular, \033[1;32m+29.99 \033[0;37mPremium "))
            pack = eval(input("\033[0;37mWould you like a cage pack? Yes(1) or No(2) Cost: \033[1;32m+$19.99  ")) 
            bone = eval(input("\033[0;37mWould you like some fish bones? Yes(1) or No(2) Cost: \033[1;32m+4.99  "))
            print()
            if cage == 1:
                Item_list.append("Regular")
                Price_list.append(80)
            elif cage == 2:
                Item_list.append("Large")
                Price_list.append(100)
            elif cage == 3:
                Item_list.append("None")
                Price_list.append(0)
            if food == 1:
                Item_list.append("Regular")
                Price_list.append(20)
            elif food == 2:
                Item_list.append("Premium")
                Price_list.append(30)
            elif food == 3:
                Item_list.append("None")
                Price_list.append(0)
            if pack == 1:
                Item_list.append("Yes")
                Price_list.append(20)
            elif pack == 2:
                Item_list.append("No")
                Price_list.append(30)
            if bone == 1:
                Item_list.append("Yes")
                Price_list.append(5)
            elif bone == 2:
                Item_list.append("No")
                Price_list.append(0)
        ask = int(input("\033[0;37mWould you like to select another Budgie(1) or proceed to the checkout(2) "))
        if ask == 1:
            Base = Base+20
        else:
            coupon_roll = eval(input("\033[0;37mWould you like to participate in our lucky discount draw? Yes(1) or No(2) "))
            if coupon_roll == 1:
                time.sleep(1)
                print("You will shortly receive your discount roll.")
                time.sleep(4)
                Total_cost = 0
                for i in range(len(Price_list)):
                    Total_cost = Total_cost + Price_list[i]
                print()
                print("\033[0;37mBird Colour:\033[1;33m",Item_list[0])
                print("\033[0;37mTraining Add-Ons:\033[1;33m",Item_list[1])
                print("\033[0;37mSpecial Add-Ons:\033[1;33m",Item_list[2])
                print("\033[0;37mServices:\033[1;33m",Item_list[3])
                print("\033[0;37mCage:\033[1;33m",Item_list[4])
                print("\033[0;37mFood:\033[1;33m",Item_list[5])
                print("\033[0;37mCage Pack:\033[1;33m",Item_list[6])
                print("\033[0;37mFish Bones:\033[1;33m",Item_list[7])
                print()
                print("\033[0;37mYour total cost is:\033[1;32m $",Total_cost, sep = '')
                time.sleep(2.5)
                discount = randint(10,40)
                saved_money = (discount/100)*Total_cost
                input("\033[1;37mPress ENTER to roll your lucky discount number!!")
                print("rolling...")
                time.sleep(5)
                print("\033[0;37mCongratulations! You now have a\033[1;32m",discount,"\033[0;37mpercent discount!")
                time.sleep(2)
                discount_percentage = (100-discount)/100
                Total_cost = round(Total_cost*discount_percentage,2)
                print("\033[0;37mYour New Total Cost is $\033[1;32m",round(Total_cost,2), "\033[0;37m. You saved ",round(saved_money,2)," dollars!", sep = '')
                print()
                if Total_cost > 150:
                    time.sleep(2)
                    print("\033[1;mSince you spent more than $150 in your purchases, you get to roll 1 \033[1;32mFREE \033[1;37mservice every week!")
                    free_roll = randint(1,5)
                    input("\033[1;37mPress ENTER to roll your free service: ")
                    time.sleep(1)
                    print("\033[1;37mSpinning your free wheel...")
                    time.sleep(5)
                    if free_roll == 1:
                        print("\033[1;33mVery nice! \033[0;37mYou now have a \033[1;32mFREE \033[0;37mnail trim!")
                    elif free_roll == 2:
                        print("\033[1;33mAwesome! \033[0;37mYou now have a \033[1;32mFREE \033[0;37mbird bath!")
                    elif free_roll == 3:
                        print("\033[1;33mAmazing! \033[0;37mYou now have a \033[1;32mFREE \033[0;37mwing trim!")
                    elif free_roll == 4:
                        print("\033[1;33mSuper! \033[0;37mYou now have a \033[1;32mFREE \033[0;37mcheck-up!")
                    elif free_roll == 5:
                        print("\033[1;33mWow! \033[0;37mYou now have a \033[1;32mFREE \033[0;37mbird daycare day!")
                else:
                    time.sleep(2)
                receipt = eval(input("Would you like your receipt? Yes(1) or no(2) "))
                if receipt == 1:
                    print("\033[1;36mGenerating receipt, please wait.")
                    time.sleep(3)
                    print()
                    print("\033[0;37mHere is your item list")
                    print("\033[0;37mBird Colour:\033[1;33m",Item_list[0])
                    print("\033[0;37mTraining Add-Ons:\033[1;33m",Item_list[1])
                    print("\033[0;37mSpecial Add-Ons:\033[1;33m",Item_list[2])
                    print("\033[0;37mServices:\033[1;33m",Item_list[3])
                    print("\033[0;37mCage:\033[1;33m",Item_list[4])
                    print("\033[0;37mFood:\033[1;33m",Item_list[5])
                    print("\033[0;37mCage Pack:\033[1;33m",Item_list[6])
                    print("\033[0;37mFish Bones:\033[1;33m",Item_list[7])
                    print()
                    print("\033[0;37mSub-Total: \033[1;32m$",round(Total_cost,3),sep = '')
                    print("\033[0;37mHST(13%): \033[1;32m$",float(round((Total_cost*0.13),2)), sep = '')
                    print("\033[0;37mTotal: \033[1;32m$",round((Total_cost*1.13),2), sep = '')
                    print()
                    print()
                    print("\033[1;37mThank you for shopping at Jerry's Budgie SuperStore! We hope to see you again!")
                    break
                else:
                    print("\033[1;37mThank you for shopping at Jerry's Budgie SuperStore! We hope to see you again!")
                    break
            else:
                Price_list.append(Base)
                Total_cost = 0
                for i in range(len(Price_list)):
                    Total_cost = Total_cost + Price_list[i]
                print()
                print("\033[0;37mHere is your item list")
                print("\033[0;37mBird Colour:\033[1;33m",Item_list[0])
                print("\033[0;37mTraining Add-Ons:\033[1;33m",Item_list[1])
                print("\033[0;37mSpecial Add-Ons:\033[1;33m",Item_list[2])
                print("\033[0;37mServices:\033[1;33m",Item_list[3])
                print("\033[0;37mCage:\033[1;33m",Item_list[4])
                print("\033[0;37mFood:\033[1;33m",Item_list[5])
                print("\033[0;37mCage Pack:\033[1;33m",Item_list[6])
                print("\033[0;37mFish Bones:\033[1;33m",Item_list[7])
                print()
                print("Your total cost is:\033[1;32m$",round(Total_cost,2), sep = '')
                if Total_cost > 150:
                    time.sleep(2)
                    print("\033[1;mSince you spent more than 150 dollars, you get to roll 1 free service every week!")
                    free_roll = randint(1,5)
                    input("Press ENTER to roll your free service ")
                    time.sleep(1)
                    print("spinning your free wheel...")
                    time.sleep(5)
                    if free_roll == 1:
                        print("\033[1;33mVery nice! \033[0;37mYou now have a \033[1;32mfree \033[0;37mnail trim!")
                    elif free_roll == 2:
                        print("\033[1;33mAwesome! \033[0;37mYou now have a \033[1;32mfree \033[0;37mbird bath!")
                    elif free_roll == 3:
                        print("\033[1;33mAmazing! \033[0;37mYou now have a \033[1;32mfree \033[0;37mwing trim!")
                    elif free_roll == 5:
                        print("\033[1;33mSuper! \033[0;37mYou now have a \033[1;32mfree \033[0;37mcheck-up!")
                    elif free_roll == 6:
                        print("\033[1;33mWow! \033[0;37mYou now have a \033[1;32mfree \033[0;37mbird daycare day!")
                else:
                    time.sleep(2)
                receipt = eval(input("Would you like your receipt? Yes(1) or no(2)"))
                if receipt == 1:
                    print()
                    print("\033[0;37mHere is your item list")
                    print("\033[0;37mBird Colour:\033[1;33m",Item_list[0])
                    print("\033[0;37mTraining Add-Ons:\033[1;33m",Item_list[1])
                    print("\033[0;37mSpecial Add-Ons:\033[1;33m",Item_list[2])
                    print("\033[0;37mServices:\033[1;33m",Item_list[3])
                    print("\033[0;37mCage:\033[1;33m",Item_list[4])
                    print("\033[0;37mFood:\033[1;33m",Item_list[5])
                    print("\033[0;37mCage Pack:\033[1;33m",Item_list[6])
                    print("\033[0;37mFish Bones:\033[1;33m",Item_list[7])
                    print()
                    print("\033[0;37mSub-Total: $\033[1;32m",round(Total_cost,2),sep = '')
                    print("\033[0;37mHST(13%): $\033[1;32m",round((Total_cost*0.13),2), sep = '')
                    print("\033[0;37mTotal: $\033[1;32m",round((Total_cost*1.13),2), sep = '')
                    time.sleep(3)
                    print("\n"*5)
                    print("\033[0;37mThank you for shopping at Jerry's Budgie SuperStore! We hope to see you again!")
                    time.sleep(3)
                    break
                else:
                    print("\033[1;37mThank you for shopping at Jerry's Budgie SuperStore! We hope to see you again!\033[0;37m")
                    break
BudgieShop()