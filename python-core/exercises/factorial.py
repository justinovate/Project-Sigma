def main():
    num = int(input("Enter a number: "))
    try:
        result = factorial(num)
        steps = " * ".join(str(x) for x in range(num, 0, -1)) if num > 1 else "1"
        print(f"{num}! = {steps} = {result}")
    except ValueError as e:
        print(e)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        raise ValueError("Undefined for negative numbers")
    else:
        # result = 1
        # for i in range(n, 1, -1):
        #     result *= i
        # return result
        return n * factorial(n - 1) # recursive approach

if __name__ == "__main__":
    main()