def variance(treatment):
    summation = 0 
    mean = sum(treatment) / len(treatment)
    for i in treatment:
        summation += (i - mean) ** 2
    return summation / (len(treatment) - 1)

t_1 = [9, 7, 3, 14, 1, 2, 0 , 9, 12, 0, 2, 5, 6, 3, 15, 7, 5, 11]
t_2 = [5, 9, 0, 3, 8, 9, 5, 2, 6, 9, 9, 7, 13, 8, 0, 5, 4, 12, 7, 5, 10, 9, 5, 2, 10]
t_3 = [2, 6, 1, 0, 4, 0, 4, 3, 3, 6, 6, 5, 9, 3, 0, 7, 4]
t_4 = [5, 1, 5, 6, 5, 1, 0, 0, 2, 4, 1, 4, 3, 3]

print(variance(t_1))
print(variance(t_2))
print(variance(t_3))
print(variance(t_4))