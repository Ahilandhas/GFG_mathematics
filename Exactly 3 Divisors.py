"""
The time complexity of this solution is O(N * sqrt(N)) because we are iterating up to sqrt(N) to find prime numbers and then iterating up to N to count numbers with exactly 3 divisors. 
The space complexity is O(sqrt(N)) for storing the boolean array isPrime
"""

import math


class Solution:
   def exactly3Divisors(self, N):
        if N <= 3:
            return 0

        # Sieve up to sqrt(N) since we only care about primes whose squares are <= N
        limit = int(math.sqrt(N))
        isPrime = [True] * (limit + 1)
        isPrime[0], isPrime[1] = False, False  # 0 and 1 are not prime

        i = 2
        while i * i <= limit:
            if isPrime[i]:
                for j in range(i * i, limit + 1, i):
                    isPrime[j] = False
            i += 1

        # Count numbers with exactly 3 divisors, i.e., primes' squares <= N
        count = 0
        for i in range(2, limit + 1):
            if isPrime[i] and i * i <= N:
                count += 1

        return count


# Example usage
solution = Solution()
print(solution.exactly3Divisors(10))  # Output: 1
