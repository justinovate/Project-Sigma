def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) 
            # break
        except ValueError:
            # print("x is not an integer")
            pass
        # else:
        #     # break
        #     return x

main()

