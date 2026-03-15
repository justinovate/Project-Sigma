def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# def is_valid(s):
#     if s[:2].isalpha():
#         if 2 <= len(s) <= 6:
#             if s.isalnum():
#                 for i in range(len(s)):
#                     if s[i].isnumeric() and int(s[i]) > 0:
#                         if s[i:].isnumeric():
#                             return True

def is_valid(s):
    conditions = [
        s.isalnum(),
        s[:2].isalpha(),
        2 <= len(s) <= 6,
    ]

    number_started = False
    
    for c in s[2:]:
        if c.isdigit():
            if not number_started:
                number_started = True
                if c == '0':
                    return False
        elif c.isalpha():
            if number_started:
                return False
            
    return all(conditions)

main()