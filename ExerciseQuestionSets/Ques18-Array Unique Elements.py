# Write Python code to remove duplicate elements from an array of integers while preserving the order of the remaining elements. Print the modified array
def removeDuplicates(arr):
    seen = set()  # To keep track of seen elements
    result = []  # To store the result

    for element in arr:
        # If the element is not in the seen set, add it to both the result and seen
        if element not in seen:
            seen.add(element)
            result.append(element)

    return result

# Test the function
exampleArray = [1, 2, 2, 3, 4, 3, 5]
modifiedArray = removeDuplicates(exampleArray)

print(f"The modified array after removing duplicates is {modifiedArray}")
