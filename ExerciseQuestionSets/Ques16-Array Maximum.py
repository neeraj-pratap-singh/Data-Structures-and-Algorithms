# Find the maximum value in an array of integers using Python. Print both the maximum value and its index.
def findMaximumValueAndIndexUsingBuiltIn(arr):
    # Find maximum value using the built-in max() function
    maxValue = max(arr)
    
    # Find the index of the maximum value using the index() method
    maxIndex = arr.index(maxValue)
    
    return maxValue, maxIndex

# Test the function with an example array
exampleArray = [10, 20, 50, 15, 40]
maxValue, maxIndex = findMaximumValueAndIndexUsingBuiltIn(exampleArray)
print(f"The maximum value in the array is {maxValue}, found at index {maxIndex}")
