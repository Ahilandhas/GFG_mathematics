"""
Time complexity -> O(n)
space complexity -> O(1)
"""


def check_prime(num:int):
    if num <= 1:
        return False
    
    for i in range(2,(num//2)+1):
         if num % i == 0:
             return False
    return True

print(check_prime(3))


"""
time complexity -> O(sqaure root(n) )
space complexity -> O(1)
"""

def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    i = 2
    while i * i <= n:  # Check up to the square root of n
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False  # n is not prime
        i += 1  # Increment i
    return True  # If no divisors found, n is prime

print(is_prime(49))

"""
super efficient
time complexity -> O(sqaure root(n) )
space complexity -> O(1)
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

print(is_prime(49))


