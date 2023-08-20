# program to list all prime numbers up to a given value n
def sieve_of_eratosthenes(n):
    prime = [True] * (n+1)
    p = 2
    
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    prime_numbers = []
    for p in range(2, n+1):
        if prime[p]:
            prime_numbers.append(p)
    
    return prime_numbers

n = int(input("Enter the value of n: "))
prime_numbers_list = sieve_of_eratosthenes(n)
print("Prime Numbers up to", n, ":", prime_numbers_list)
# The time complexity of the Sieve of Eratosthenes algorithm is O(n log log n), where n is the value up to which you want to find prime numbers.