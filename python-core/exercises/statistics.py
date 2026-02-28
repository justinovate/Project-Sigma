def stddev(x):
    sum = 0
    for i in x:
        sum += (i - 7.1) ** 2

    s = (1 / (len(x) - 1) * sum) ** 0.5
    print(f"Standard Deviation: {s:.4f}")

x_3 = [6, 8, 7, 5, 6, 4, 7, 8, 5, 6]
x_4 = [9, 8, 5, 7, 6, 5, 7, 8, 9, 7]

# stddev(x_3)
stddev(x_4)