def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[:2].isalpha():
        if 2 <= len(s) <= 6:
            if s.isalnum():
                for i in range(len(s)):
                    if s[i].isnumeric() and int(s[i]) > 0:
                        if s[i:].isnumeric():
                            return True

main()