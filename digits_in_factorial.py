"""
Given an integer N. Find the number of digits that appear in its factorial. 
Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.
 

Example 1:

Input: N = 5
Output: 3
Explanation: Factorial of 5 is 120.
Number of digits in 120 is 3 (1, 2, and 0)
"""

#User function Template for python3

# class Solution:
#     def digitsInFactorial(self,N):
#         # code here
#         A = 1
#         for i in range(N):
#             A = (i+1)*A
#         B = len(str(A))
#         return B

#User function Template for python3
import math
class Solution:
    def digitsInFactorial(self,N):
        if N == 0 or N==1:
            return 1
        log_sum = 0
        for i in range(2,N+1):
            log_sum += math.log10(i)
        return math.floor(log_sum)+1

solution = Solution()
solution.digitsInFactorial(N)
