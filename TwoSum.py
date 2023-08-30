# WAP using python for following statement
# Given are an array of integers and target sum, find 2 numbers that can be add up and return target sum, provide the indices of those number
def two_sum(nums, target):
    # Create an empty dictionary to store visited elements and their indices
    visited = {}
    
    # Loop through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement of the current number with respect to the target sum
        complement = target - num
        
        # If the complement exists in the visited dictionary, return its index along with the current index
        if complement in visited:
            return [visited[complement], i]
        
        # Otherwise, add the current number and its index to the visited dictionary
        visited[num] = i
    
    # If no such pair of indices exist, return None
    return None

# Test the function
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)
