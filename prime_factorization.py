"""
Prime factorization is the process of breaking down a number into the product of its prime numbers.

The time complexity of the prime_factors function is O(n * sqrt(n)
The space complexity of the function is O(1)

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

def prime_factors(num):
    for i in range(2,num+1):
        if is_prime(i):
            x = i
            while num % x == 0:
                print(i)
                x = x * i

prime_factors(100)


----------------------------------- ---------------- ------------------------

"""
The time complexity of this function is O(sqrt(n))
Space complexity -> o(log(n))
"""

def prime_factors(n):
    factors = []

    # Handle factor of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle factor of 3
    while n % 3 == 0:
        factors.append(3)
        n //= 3

    # Check for factors of the form 6k ± 1
    i = 5
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= (i + 2)
        i += 6

    # If n becomes a prime number greater than 3
    if n > 1:
        factors.append(n)

    return factors


number = 100
print(f"Prime factors of {number}: {prime_factors(number)}")




