def find_missing_number_and_index(original_array, given_array):
    # Find the missing number by comparing both arrays
    for i in range(len(original_array)):
        if i >= len(given_array) or original_array[i] != given_array[i]:
            return original_array[i], i  # Return the missing number and its index
    return None, -1  # In case no missing number is found

# Taking user input
n = int(input("Enter the size of the original sequence (including the missing number): "))
original_array = list(map(int, input(f"Enter {n} numbers of the original array separated by spaces: ").split()))
given_array = list(map(int, input(f"Enter {n-1} numbers of the array (with one missing number) separated by spaces: ").split()))

# Finding the missing number and its index
missing_number, index = find_missing_number_and_index(original_array, given_array)

if missing_number is not None:
    print(f"The missing number is: {missing_number}")
    print(f"The missing number was at index: {index}")
else:
    print("No missing number found.")
