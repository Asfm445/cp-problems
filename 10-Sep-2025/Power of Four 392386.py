# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        def func(n):
            if n==1 or n==0:
                return True
            if n%4!=0:
                return False
            else:
                return func(n/4)
        return  func(n)
        