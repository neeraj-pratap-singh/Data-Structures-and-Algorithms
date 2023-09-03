# Create an empty list in Python and add elements to it to create an array of integers. Demonstrate how to append, insert, and remove elements from the array.
# Initialize an empty list
integerList = []

# Append elements (Adds elements to the end)
integerList.append(1)
integerList.extend([2, 3, 4])
print(f"After appending elements: {integerList}")  # Output: [1, 2, 3, 4]

# Insert elements (Inserts elements at a specific index)
integerList.insert(0, 0)  # Insert 0 at the beginning
integerList.insert(2, 5)  # Insert 5 at index 2
print(f"After inserting elements: {integerList}")  # Output: [0, 1, 5, 2, 3, 4]

# Remove elements
integerList.remove(5)  # Remove first occurrence of 5
print(f"After removing 5: {integerList}")  # Output: [0, 1, 2, 3, 4]

# Remove element at specific index using pop()
removedElement = integerList.pop(0)  # Remove and return element at index 0
print(f"Removed element: {removedElement}")  # Output: Removed element: 0
print(f"After removing element at index 0: {integerList}")  # Output: [1, 2, 3, 4]
