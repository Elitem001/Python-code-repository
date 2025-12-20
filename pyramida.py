rows = int(input("Enter the number of rows: "))

for j in range(rows):
    for i in range(rows - j - 1):
        print(" ", end= " ")
    for g in range(2 * j + 1):
        print("*", end =" ")
    print()

   
