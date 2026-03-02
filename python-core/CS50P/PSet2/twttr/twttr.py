prompt = input("Input: ")
output = ""
for character in prompt:
    if character in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        character = ""
        output += character
    else:
        output += character
print(f"Output: {output}")