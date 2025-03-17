def is_palindrome(n):
    return str(n) == str(n)[::-1] 
# Convert to string and check if it equals its reverse

# Taking user input
num = int(input("Enter a number: "))

# Checking and printing the result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
