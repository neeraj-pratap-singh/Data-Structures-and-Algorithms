# Print 1D array and 2D array using for loop
# 1D array
numbers = [12, 34, 45, 67, 87, 98]
print("1D Array:")
for num in numbers:
    print(num, end=" ")
print()  # Print a new line after the array is printed

# 2D array
matrix = [[12, 34, 45], [23, 45, 67], [34, 56, 78]]
print("2D Array:")
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # Print a new line after each row
