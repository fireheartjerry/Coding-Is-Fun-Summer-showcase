import random
def setup_question_bank():
   tbag_questions = [
       ["True/False: Europe has no deserts. ", ["True", "true"]],
       ["How many seasons does Friends have? ", ["10", "Ten", "ten"]],
       ["What is the largest organ? ", ["skin", "Skin"]],
       ["What is the most copied link on the internet? (just write one word) ", ["rickroll",
                                                                                 "Rickroll", "RickRoll"]],
       ["True/False: Albert Einstein had trouble with mathematics in school. ", ["False", "false"]],
       ["What Youtube video has the most views? ", ["Baby Shark Dance", "baby shark dance"]],
       ["How many hearts does an octopus have? ", ["3", "three", "Three"]]
   ]
   return tbag_questions
def bonus_question_setup():
    bonus_questions = [
        ["What is your personality(Myers Briggs Type Indicator, MBTI)",["ISTP-T","ISTP"]],
        ["What is the largest Metropolitan Area in terms of Population?",["Tokyo","tokyo"]],
        ["What is 1+1",["2","Two","two"]]
    ]  
    return bonus_questions
question_bank = setup_question_bank()
bonuse_question_bank = bonus_question_setup()
hp_point = random.randint(7,10)
def rules ():
    print('\t☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆')
    print("\t\t\tWelcome to TBAG")
    print('\t☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆')
    print("Instructions:")
    print("1. This game is to answer questions\n"
          "2. You start with a random number of HP\n"
          "\t- for each correct answer, you gain 3 points,\n"
          "\t- otherwise you lose 3 points\n"
          "3. If your HP reaches 18 points, you win\n"
          "4. If your HP reaches 0 point, you lose")
    print("*************************************************\n")
rules()
question_counter = 0
bonus_counter = 0
while (hp_point > 0) and (hp_point < 18):
    question_number = random.randint(0, 6)
    bonus_counter = random.randint(0,2)
    question_counter += 1
    count = random.randint(1,2)
    if count == 1:
        print(question_bank[question_number][0])
        answer = input("What is your answer: ")
        if answer in question_bank[question_number][1]:
            hp_point += 3
            print("you answered correctly. health left: ", hp_point)
            print()
        else:
            hp_point -= 3
            print("you didn't answer correctly. health left: ", hp_point)
            print()
    else:
        print(bonuse_question_bank[bonus_counter][0])
        print("BONUS QUESTION, +3 points")
        bonuse_answer = input("What is your answer: ")
        if bonuse_answer in bonuse_question_bank[bonus_counter][1]:
            hp_point += 6
            print("You answered correctly. health left:", hp_point)
            print()
        else:
            hp_point -= 6
            print("you didn't answer correctly. health left: ", hp_point)
            print()
if hp_point <= 0:
    print("You're dead. Rest in peace.")
else:
    print("Gud job. You made it to ze end! But ur still died. Rest in peace")