numbers = []
count = int(input("How many numbers would you like to check? "))
for i in range(count):
    i = int(input(f"Enter {i+1}th item: "))
    numbers.append(i)
new_list = []
for number in numbers:
    if number < 5:
        new_list.append(number)
print("Numbers less than 5")
print(new_list)