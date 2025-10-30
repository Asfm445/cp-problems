# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

from math import *
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=int(1e9+7)
        if n==1:
            return 5
        def func(a,b):
            if b<=1:
                return 1
            ans=func(a,b//2)
            if b%2==0:
                ans*=ans*a%mod
            else:
                ans*=ans*a*a%mod
            return ans
        if n%2==0:
            a=n//2
            b=n//2
        else:
            a=n//2+1
            b=n//2
        return 5*func(5,a)*4*func(4,b)%mod

