# Problem: Heaters - https://leetcode.com/problems/heaters/

from math import *

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def check(m):
            i=0
            k=0
            while i<len(houses):
                if houses[i]<heaters[k]-m:
                    return False
                if houses[i]>heaters[k]+m:
                    k+=1
                    if k==len(heaters):
                        return False
                else:
                    i+=1
            return True
        
        if len(houses)==1:
            return 0

        l=0
        r=int(1e9)
        while l<=r:
            m=l+(r-l)//2
            if check(m):
                print(check(m))
                r=m-1
            else:
                l=m+1
        return l