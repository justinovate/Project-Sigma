num_terms = int(input("Enter the number of terms to generate: "))

previous = 0
current = 1

for _ in range(num_terms):
    print(previous, end=" ")
    next_value = previous + current
    previous = current
    current = next_value