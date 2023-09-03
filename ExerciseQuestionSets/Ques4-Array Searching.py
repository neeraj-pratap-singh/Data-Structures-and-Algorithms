# Given an array of integers and a target value, write a Python function to find the index of the target value in the array using binary search. Ensure that the array is sorted before applying binary search.
def binarySearch(array, target):
    # First, sort the array
    sortedArray = sorted(array)
    
    # Initialize pointers for the start and end of the array
    startIndex = 0
    endIndex = len(sortedArray) - 1
    
    # Perform binary search
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2  # Find the middle index
        
        if sortedArray[midIndex] == target:
            return midIndex  # Target value found, return its index
        
        elif sortedArray[midIndex] < target:
            startIndex = midIndex + 1  # Narrow down to the right half
            
        else:
            endIndex = midIndex - 1  # Narrow down to the left half
    
    return -1  # Target value not found, return -1

# Test the function
testArray = [4, 2, 7, 1, 9, 3]
targetValue = 7
result = binarySearch(testArray, targetValue)

if result != -1:
    print(f"The target value {targetValue} is at index {result} in the sorted array.")
else:
    print(f"The target value {targetValue} is not found in the array.")
