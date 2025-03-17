# Program demonstrating 2D array
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# here we are Printing the 2D array
print("The elements of the 2D array are:")
for row in arr:
    for element in row:
        print(element, end=" ")
    print()  # Move to the next line after printing a row
