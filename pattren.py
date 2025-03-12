def pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

# Number of rows for the pyramid
rows = int(input("Enter the number of rows: "))
pyramid(rows)
#Reverse of pattren
print("reverse of pattren")
def reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "* " * i)

# Number of rows for the reverse pyramid
rows = int(input("Enter the number of rows: "))
reverse_pyramid(rows)
