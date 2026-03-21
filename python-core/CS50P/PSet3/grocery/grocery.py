grocery_list = []

while True:
    try:
        item = input()
        grocery_list.append(item)
    except EOFError:
        break

grocery_list.sort()

current = None
count = 0

for item in grocery_list:
    if item != current:
        if current is not None:
            print(count, current.upper())
        current = item
        count = 1
    else:
        count += 1

# print last item
if current is not None:
    print(count, current.upper())