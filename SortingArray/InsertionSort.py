def insertionSort(arr):
    """ Sorts the input array using the Insertion Sort algorithm. """
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be sorted
        j = i - 1  # Initialize j to the element before i
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key at its correct position
        arr[j + 1] = key

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
insertionSort(arr)
print("Sorted array:", arr)
