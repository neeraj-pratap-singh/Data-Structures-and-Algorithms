# Write a Python function that takes an array of integers as input and returns the sum of all the elements in the array. Optimize the function for large arrays.
def sumOfArray(integerArray):
    return sum(integerArray)

# Take the size of the array from the user
arraySize = int(input("Enter the size of the array: "))

# Initialize an empty list
userArray = []

# Take array elements from the user
for i in range(arraySize):
    element = int(input(f"Enter element {i + 1}: "))
    userArray.append(element)

# Calculate and print the sum
result = sumOfArray(userArray)
print(f"The sum of the array is: {result}")
