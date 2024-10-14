"""
Time complexity -> O(n)
"""
x = 7
temp = x

def funtion_palindrome(x,temp):
    r = 0
    while temp :

        ld = temp % 10

        r = r* 10 + ld

        temp = temp // 10
    print(r)
    return x == r

print(funtion_palindrome(x,temp))


"""
The time complexity of the is_palindrome function is O(log₁₀(n))
"""

def palindrome(n:int) ->bool:

    if n < 0 or n % 10 == 0 and n != 0:
        return False

    reversed_number = 0

    while n > reversed_number:
        reversed_number = reversed_number * 10 + n % 10
        n = n // 10

    return n == reversed_number or reversed_number // 10 == n

print(palindrome(111))


"""
The time complexity of the is_palindrome function is O(n)
The time complexity of this function is O(n) because the function converts the integer n to a string and then compares the original string with its reverse. 
The space complexity is also O(n) because the function creates a new string of length n to store the reversed version of the original string
"""

def palindrome(n:int) ->bool:

    return str(n)[:] == str(n)[::-1]

print(palindrome(1212321))
