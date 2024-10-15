"""
The greatest common divisor (GCD) of two or more numbers is the greatest common factor number that divides them, exactly. 
It is also called the highest common factor (HCF). 
For example, the greatest common factor of 15 and 10 is 5, since both the numbers can be divided by 5.

Steps for Euclidean Algorithm:
    Divide the larger number by the smaller number.
    Find the remainder of this division.
    Replace the larger number with the smaller number, and the smaller number with the remainder from step 2.
    Repeat the process until the remainder is zero.
    The last non-zero remainder is the GCD.
"""

"""
gcd using euclien algorithm -> O(log(min(a,b))
"""

def gcd(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b -a

    return a


print(gcd(12,5))

"""
optimised euclien algorithm -> O(log(min(a,b))
"""

def gcd(a,b):
    if b == 0:
        return a

    return gcd(b,a%b)

print(gcd(10,5))


"""
LCM

naive approch

time complexity -> theta(a*b - max(a,b))
"""

def lcm(a,b):
    res = max(a,b)

    while True:
        if res % a == 0 and res % b == 0 :
            return res

        res+=1


print(lcm(4,1))

"""
Efficent approach
GCD or GCF Method of Finding LCM
This method is used only when the greatest common factor of two numbers is given. The formula used to find the LCM using the GCF or GCD is:

L.C.M. = a×b/ gcd(a,b)

For example, for 15 and 24, the GCF will be 3. So, the LCM will be (15 × 24) / 3 = 3.
time complexity O(log(min(a,b))

"""

def gcd(a,b):
    if b == 0:
        return a

    return gcd(b,a%b)


def lcm(a,b):
    return a * b // gcd(a,b)

a = 4
b = 101
print(lcm(a,b))

#--------------- ---------------------------- ----



