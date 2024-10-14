"""
time complexity logn
space o(n)

Recursive approch
"""
def findpower(x,n):

    if n == 0:
        return 1

    temp = findpower(x,n//2)
    temp = temp * temp

    if n % 2 == 0:
        return temp

    else:
        return temp * x

print(findpower(3,1))

#------- - ------------------- ---------------

"""
time complexity - logn
space complexity- logn
Iterative approch,(Binary Exponentiation)
"""

def power(x,n):
    res = 1
    while n > 0:
        if n % 2 !=0:
            res = res * x

        x = x * x
        n = n // 2

    return res

print(power(3,3))
