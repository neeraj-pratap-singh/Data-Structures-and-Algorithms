# Write a Python function that calculates the sum of all the elements in an array of integers. Test it with an example array.
def calculateArraySum(arr):
    # Initialize sum to 0
    totalSum = 0
    
    # Loop through each element in the array and add it to the sum
    for num in arr:
        totalSum += num
        
    return totalSum

# Test the function with an example array
exampleArray = [1, 2, 3, 4, 5]
result = calculateArraySum(exampleArray)
print(f"The sum of all elements in the array is: {result}")
