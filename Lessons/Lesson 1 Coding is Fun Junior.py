hour = int(input("Enter the time it is(PM add 12): "))
if 0 <= hour < 12:
    print("Good morning!")
elif 18 > hour >= 12:
    print("Good afternoon!")
elif 24 > hour >= 18:
    print("Good evening!")
print()

random = ["apple", "banana", "cherry", 1, 2, 3]
i = 0
while i < 6:
    print(random[i], end=' ')
    i += 1

L = ["apple", "banana", "cherry", 1, 2, 3]
for item in L:
    print(item, end=' ')
print()