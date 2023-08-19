# Program to reverse a array using for loop
numbers = [12, 34, 45, 67, 87, 98]

# Find the length of the array
length = len(numbers)

# Initialize an empty list to store the reversed array
reversed_numbers = [0] * length

# Iterate through the original array in reverse order
for i in range(length):
    reversed_numbers[length - 1 - i] = numbers[i]

print(reversed_numbers)
