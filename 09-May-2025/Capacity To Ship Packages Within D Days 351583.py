# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysNeed(m):
            days=1
            w=0
            for i in weights:
                w+=i
                if w>m:
                    days+=1
                    w=i
                    # print(w)
            return days



        l=max(weights)
        r=sum(weights)


        while l<=r:
            m=l+(r-l)//2
            if daysNeed(m)<=days:
                r=m-1
            else:
                l=m+1
                
        return l