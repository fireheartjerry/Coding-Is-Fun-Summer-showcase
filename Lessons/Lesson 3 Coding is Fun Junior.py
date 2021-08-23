# Lesson 3
# Exercise 1
def Kilometer_convert(miles):
    kilometers = miles * 1.6
    print(f"{float(kilometers)} miles is {miles} kilometers")
    print()


Kilometer_convert(eval(input("Enter how many miles you have: ")))

# Exercise 2
Question_list = [
    ["True/False, Europe has no deserts.", ["True", "true"]],
    ["How many seasons does Friends have", ["Ten", "ten", 10]],
    ["What is the largest organ", ["Skin", "skin"]],
    ["What is the most copied link on the internet(1 word)", ["Rickroll", "rickroll", "RickRoll"]],
    ["True/False Albert Einstein had trouble with math", ["False", "false"]],
    ["How many hearts does an octopus have", [3, "Three", "three"]]
]
print(Question_list[2][1])



