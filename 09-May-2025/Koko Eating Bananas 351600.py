# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s=sum(piles)
        l=s//h
        r=max(piles)


        def canfinish(m):
            hr=h
            for i in piles:
                if i>m:
                    if i%m==0:
                        hr-=(i//m)
                    else:
                        hr-=(i//m+1)
                else:
                    hr-=1
            if hr>=0:
                return True
            return False



        if h>s:
            return 1
        while l<=r:
            m=l+(r-l)//2
            if canfinish(m):
                r=m-1
            else:
                l=m+1
        print(l)
        return l