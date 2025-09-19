# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # Keep dividing n by powers of 5 and add the quotient to the count
        divisor = 5
        while divisor <= n:
            count += n // divisor
            divisor *= 5
        return count