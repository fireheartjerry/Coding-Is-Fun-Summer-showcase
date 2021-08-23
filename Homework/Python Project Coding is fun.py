# =============================================================================
# Python Project
# 2021-04-21
# Entry Quiz
# =============================================================================
def AddSub():
    balance = "q"
    while balance != "Q":
        start = eval(input("\033[1;36mWould you like to play(1) or exit(2): "))
        if start == 1:
            sum = 0
            i = 2
            N = int(input("\033[1;32mEnter your maximum number: "))
            while i < N+1:
                if i%2 == 1:
                    i = i*-1
                else:
                    i = i
                sum = sum+i
                i = abs(i)+1
            print()
            print("\033[1;35mThe total is:",sum)
            print()
        elif start == 2:
            balance = "Q"
            return("\033[1;33mYou ended the program.")
        else: 
            print("\033[1;31mThat is not an option, please try again.")
            print()
print()
print()
print("\033[1;34mWelcome to this program, enjoy!")
print()
print()
print(AddSub())
