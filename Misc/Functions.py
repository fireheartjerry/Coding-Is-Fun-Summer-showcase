def fact(Limit):
    Product = 1
    for i in range(Limit,1,-1):
        Product = Product*i
    return(Product)

factorial = eval(input("Enter your factorial number: "))
print(fact(factorial))

def DivCheck():
    letter = "q"
    while letter != "Q":
        ask = int(input("Would you like to check(1) or quit(2): "))
        if ask == 1:
            number = eval(input("Enter your divisibility checking number: "))
            divide = eval(input("Enter your number: "))
            if number%divide == 0:
                print(number,"is divisible by",divide)
                print()
            else:
                print(number,"is not divisible by",divide)
                print()
        elif ask == 2:
            print("You ended the program")
            letter = "Q"
DivCheck()

num = eval(input("Enter your prime number check: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
   print(num,"is not a prime number")