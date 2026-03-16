def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if not s.isalnum():
        return False
    
    if not s[:2].isalpha():
        return False
    
    if not (2 <= len(s) <= 6):
        return False
    
    number_started = False

    for c in s[2:]:
        if c.isdigit():
            if not number_started:
                number_started = True
                if c == '0':
                    return False
        elif number_started:
            return False
    
    return True

main()