#Armstrong_Number_check
def is_armstrong(num):
    num_str = str(num)  # Convert number to string to count digits
    power = len(num_str)  # Get the number of digits
    armstrong_sum = sum(int(digit) ** power for digit in num_str)  # Compute sum of powered digits
    return num == armstrong_sum  # Check if it equals the original number

# Taking user input
num = int(input("Enter a number: "))
# Checking and printing the result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
