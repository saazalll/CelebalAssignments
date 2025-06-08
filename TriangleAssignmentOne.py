#Assignment 1
#Print the triangle pattern.

rows = 5

#for lower triangular

print("lower triangular")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("\n")


#for upper triangular

print("upper triangular")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j < i:
            print(" ", end="  ")
        else:
            print("*", end=" ")
    print()

print("\n")


#for pyramid pattern

print("pyramid pattern")
for i in range(1, rows + 1):

    for space in range(rows - i):
        print(" ", end=" ")


    for star in range(2 * i - 1):
        print("*", end=" ")
    print()
