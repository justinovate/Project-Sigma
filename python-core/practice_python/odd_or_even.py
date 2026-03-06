num = int(input("Enter a number: "))
check = int(input("Enter another number: "))

if num % 4 == 0:
    print(f"{num} is even and a multiple of 4.")
elif num % 2 == 0:
    print(f"{num} is even.")  
else:
    print(f"{num} is odd.")

if check != 0:
    if num % check == 0:
        print(f"{check} divides evenly into {num}.")
else:
    print("Cannot divide by 0.")