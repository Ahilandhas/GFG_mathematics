
"""
Naive Approch
Time complexity -> O(n)
Space complexity -> O(1)
"""

def divisors_of_numbers(n):
    for i in range(1,n+1):
        if  n % i == 0:
            print(i)

divisors_of_numbers(10)


"""
time complexity -> o ( square root(n))

space -> 0(1)

Note: output will unsorted.
"""

def divisors_of_number(num):
    divisors = []
    i = 1
    
    # Only iterate up to sqrt(num)
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)  # Add i as a divisor
            if i != num // i:    # Add num // i only if it's different
                divisors.append(num // i)
        i += 1

    return divisors

# Example usage
num = 30
print(f"Divisors of {num}: {divisors_of_number(num)}")



"""
time complexity -> o ( square root(n))

space -> 0(1)

Note: output will sorted.

"""


def divisors_of_number(num):
    i = 1

    # First print smaller divisors up to sqrt(num)
    while i * i <= num:
        if num % i == 0:
            print(i, end=" ")  # Print the smaller divisor
        i += 1

    #print(f"i {i}")
    # Then print larger divisors in reverse order (above sqrt(num))
    i -= 1
    while i >= 1:
        if num % i == 0 and i != num // i:  # Avoid duplicates for perfect squares
            print(num // i, end=" ")
        i -= 1
      

# Example usage
num = 30
divisors_of_number(num)

