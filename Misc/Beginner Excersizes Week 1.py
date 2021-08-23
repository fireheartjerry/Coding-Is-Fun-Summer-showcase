'''Question 1'''
def NumberProduct(num1, num2):
    if num1*num2 > 1000:
        print("Your sum is:",num1+num2)
    else:
        print("Your product is:",num1*num2)
NumberProduct(eval(input("Enter your first number: ")),eval(input("Enter your second number: ")))
print()

'''Question 2'''
def MultiAdd(MAX):
    for i in range(1,MAX+1):
        print(i+i-1)
MultiAdd(eval(input("Enter your number limit: ")))
print()

'''Question 3'''
def HalfString(SSS):
    for i in range(0,len(SSS)-1,2):
        print(SSS[i])
HalfString(input("Enter your string: "))
print()

'''Question 4'''
def CharErase(S1, n):
    return(S1[n:])
CharErase(input("Enter a string: "), eval(input("Enter the number of charecters you want to remove: ")))
print()

'''Question 5'''
def ListCheck(list):
    if list[0] == list[-1]:
        return("True")
    elif list[0] != list[-1]:
        return("False")
print(ListCheck(eval(input("Enter a list of integers: "))))
print()

'''Question 6'''
def DivBy5(L):
    for i in range(len(L)):
        if L[i]%5 == 0:
            print(L[i])
DivBy5(eval(input("Enter a list of numbers(with [] first): ")))
print()

'''Question 7'''
def StrCount(string, sub_string):
    string_count = string.count(sub_string)
    if string_count == 1:
        print("\033[1;32m",sub_string," \033[1;37mwas counted ","\033[1;32monce\033[1;37m in your given string.", sep = '')
given = input("\033[1;37mEnter a given string to check the number of sub-strings: ")
sub_string = input("\033[1;37mEnter a sub string to count the number of these in the given string: ")
StrCount(given, sub_string)
print()

'''Question 8'''
def numPattern(max):
    for i in range(1,max+1):
        print("\033[1;35m",(str(i)+" ")*i)
numPattern(eval(input("\033[1;37mEnter your pattern limit: ")))
print()

'''Question 9'''
def reverseCheck(num):
    if num == num[::-1]:
        print("\033[1;32mThe original and reversed number are the same.")
    elif num != num[::-1]:
        print("\033[1;31mThe original and reversed number are not the same.")
reverseCheck((input("\033[1;37mEnter your number: ")))
print()

'''Question 10'''
def OddEvenAdd(list1, list2):
    new_list = []
    for i in range(len(list1)):
        if list1[i]%2 == 1:
            new_list.append(list1[i])
        else:
            list1[i] = list1[i]
    for i in range(len(list2)):
        if list2[i]%2 == 0:
            new_list.append(list2[i])
        else:
            list2[i] = list2[i]
    print("\033[1;34m",new_list, sep = '')
LIST = eval(input("\033[1;37mEnter a list of numbers(with [] first): "))
LIST2 = eval(input("Enter a list of numbers(with [] first): "))
OddEvenAdd(LIST, LIST2)
print()

'''Question 11'''
def ReverseSpace(int):
    for i in range(len(int)-1,-1,-1):
        print("\033[1;33m",int[i], end = " ")
ReverseSpace((input("\033[1;37mEnter an integer: ")))
print()

'''Question 12'''
def TaxCalculate(Total):
    if Total < 10000:
        print("\033[0;37mYour total tax is \033[1;32m$0.00")
    elif Total <= 20000:
        print("\033[0;37mYour total tax is \033[1;32m$1000.00")
    elif Total > 20000:
        Rest = Total - 20000
        Sub_Tax = (Rest*20)/100
        Total_Tax = Sub_Tax + 1000
        print("\033[0;37mYour total tax is \033[1;32m$",float(Total_Tax),"0\033[1;37m", sep = '')
TaxCalculate(eval(input("\033[1;37mEnter your total income: ")))
print()

'''Question 13'''
def MultiTable(Limit1, Limit2):
    for j in range(1,Limit1+1):
        for i in range(1,Limit2+1):
            print("\033[1;33m",i*j, end = " ")
        print()
MultiTable(eval(input("\033[1;37mEnter your x-axis multiplication table limit: ")),eval(input("Enter your y-axis multiplication table limit: ")))
print()

'''Question 14'''
def InvertedPyramid(Size):
    for i in range(Size,0,-1):
        print("\033[1;36m* "*i,)
InvertedPyramid(eval(input("\033[1;37mEnter your size: ")))
print()

'''Question 15'''
def Exponent(base, exp):
    power = 1
    sum = 0
    while sum < exp:
        power = power*base
        sum = sum+1
    print("\033[1;32m",base," \033[0;37mto the exponent of\033[1;32m ",sum," \033[0;37mis:\033[1;32m ",power, " \033[0;37m", sep = '')
Exponent(eval(input("\033[1;37mEnter your base number: ")), eval(input("Enter your exponent: ")))