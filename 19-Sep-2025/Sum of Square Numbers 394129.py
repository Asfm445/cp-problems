# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

from math import *
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=1
        b=int(sqrt(c))
        if int(sqrt(c))==sqrt(c):
            return True
        else:
            while a<=b:
                s=a**2+b**2
                if s>c:
                    b-=1
                elif s<c:
                    a+=1
                else:
                    return True
                    break
            else:
                return False
