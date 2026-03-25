from datetime import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))
num = int(input("Enter a number: "))

year = datetime.now().year + (100 - age)
print((name + ", you will be 100 years old in the year " + str(year) + ".\n") * num)