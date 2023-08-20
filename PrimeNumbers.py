# Program to list all prime numbers up to a given value n
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def list_primes(n):
    prime_numbers = []
    for num in range(2, n+1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

n = int(input("Enter the value of n: "))
prime_numbers_list = list_primes(n)
print("Prime Numbers up to", n, ":", prime_numbers_list)
# complexity is O(n) where n is the number you're checking for primality