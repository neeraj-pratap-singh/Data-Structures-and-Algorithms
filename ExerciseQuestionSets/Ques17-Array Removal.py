# Given an array of integers, remove all occurrences of a specific value using Python. Print the modified array.
def removeOccurrences(arr, valueToRemove):
    # Use list comprehension to remove all occurrences of valueToRemove
    modifiedArray = [x for x in arr if x != valueToRemove]
    return modifiedArray

# Test the function
exampleArray = [1, 2, 3, 4, 5, 3, 6]
valueToRemove = 3

modifiedArray = removeOccurrences(exampleArray, valueToRemove)
print(f"The modified array after removing all occurrences of {valueToRemove} is {modifiedArray}")
