# Implement a Python function to sort an array of integers using the quicksort algorithm. Include both the recursive and iterative versions of the algorithm.
# Partition function
# The role of this function is to take the first element as the pivot,
# place all smaller elements to the left of the pivot,
# and all greater elements to the right of the pivot.
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    # Infinite loop to keep swapping elements until we find the correct position for the pivot
    while True:
        # Increment 'left' index while the element at 'left' is less than the pivot
        while left <= right and arr[left] <= pivot:
            left = left + 1
        # Decrement the 'right' index while the element at 'right' is greater than the pivot
        while arr[right] >= pivot and right >= left:
            right = right - 1
        # If there is an element larger on the left of the pivot
        # and an element smaller on the right, let's swap them
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # Swap pivot to the final position (i.e., 'right' index)
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Recursive Quicksort Function
# Sorts elements from 'low' to 'high' in the array 'arr'
def quicksortRecursive(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        # Sort the left partition
        quicksortRecursive(arr, low, pivotIndex - 1)
        # Sort the right partition
        quicksortRecursive(arr, pivotIndex + 1, high)

# Iterative Quicksort Function
# Sorts elements from 'low' to 'high' in the array 'arr'
def quicksortIterative(arr, low, high):
    # Stack for keeping track of low and high
    stack = []
    # Push initial low and high onto stack
    stack.append((low, high))

    # Keep popping from stack and sorting, until stack is empty
    while stack:
        low, high = stack.pop()
        if low < high:
            pivotIndex = partition(arr, low, high)
            # Push bounds of left partition
            stack.append((low, pivotIndex - 1))
            # Push bounds of right partition
            stack.append((pivotIndex + 1, high))

# Test the Recursive Quicksort Function
arr1 = [3, 6, 8, 10, 1, 2, 1]
quicksortRecursive(arr1, 0, len(arr1) - 1)
print("Sorted array using recursive quicksort:", arr1)

# Test the Iterative Quicksort Function
arr2 = [3, 6, 8, 10, 1, 2, 1]
quicksortIterative(arr2, 0, len(arr2) - 1)
print("Sorted array using iterative quicksort:", arr2)
