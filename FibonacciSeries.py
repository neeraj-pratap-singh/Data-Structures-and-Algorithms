# program to generate the Fibonacci series up to a given value n.
def fibonacci_series(n):
    fib_series = [0, 1]  # Initialize the Fibonacci series with first two terms

    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

n = int(input("Enter the value of n: "))
fibonacci_sequence = fibonacci_series(n)
print("Fibonacci Series:", fibonacci_sequence)
# The time complexity of this code is linear (O(n))
