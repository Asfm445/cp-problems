# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        def func(a,b):
            if b==1:
                return 1
            ans=func(a,b//2)
            if b%2==0:
                ans*=ans*a
            else:
                ans*=ans*a*a
            return ans
        # if n==0:
        #     return 1.0:
        if n==1:
            return x
        elif n>0:
            return x*func(x,n)
        elif n<0:
            return 1/(x*func(x,-n))
                