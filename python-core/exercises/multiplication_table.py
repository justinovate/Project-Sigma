rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for i in range(1,rows+1):
    for j in range(1,cols+1):
        print(i*j, end="\t")
    print()