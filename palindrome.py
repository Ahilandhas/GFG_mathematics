
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
