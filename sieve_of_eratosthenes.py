"""
prime number in range
time complexity -> O ( n * sqaure root(n))
"""

def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    if n == 1:
        return False
    if n == 2 or n  == 3 :
        return True
    if n % 2 == 0  or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:  # Check up to the square root of n
        if n % i == 0 or n % (i+2)==0:  # If n is divisible by i, it's not prime
            return False  # n is not prime
        i += 6  # Increment i
    return True  # If no divisors found, n is prime

def print_prime(num):
    for i in range(2,num+1):
        if is_prime(i):
            print(i,end=" ")


print_prime(100)



"""
Efficient way to find the prime numbers between the range
The time complexity is O(n log log n)
Space complexity -> O(n)
"""

def sieve(n: int) -> None:
    if n <= 1:
        return

    # Initialize the isPrime list, marking all numbers as True initially
    isPrime = [True] * (n + 1)  # isPrime[i] will be True if i is prime

    isPrime[0], isPrime[1] = False, False  # 0 and 1 are not primes

    i = 2

    # Loop over numbers up to sqrt(n)
    while i * i <= n:
        if isPrime[i]:  # If i is prime
            # Mark multiples of i as non-prime starting from i*i
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
        i += 1

    # Output the primes
    for j in range(2, n + 1):
        if isPrime[j]:
            print(j)


# Example usage
sieve(30)



