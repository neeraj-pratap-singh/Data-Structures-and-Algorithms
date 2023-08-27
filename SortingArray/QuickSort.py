# Time Complexity: O(n^2) worst-case, O(n log n) average-case

def quickSort(arr):
    # Base case: If the array is empty or contains a single element, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Choose the first element as the pivot
    pivot = arr[0]
    left = []
    right = []
    middle = []

    # Partition the array into three parts: < pivot, == pivot, > pivot
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    # Recursively sort the left and right partitions, and combine them with the middle
    return quickSort(left) + middle + quickSort(right)

# Example usage
arr = [70, 65, 12, 100, 70]
print('Unsorted array' , arr)
print('Sorted array using Quick Sort' , quickSort(arr))
