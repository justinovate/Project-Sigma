user_input = input("Input: ")
print("Output: ", end="")
for c in user_input:
    if c.lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        print(c, end="")