# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        start=n-limit*2
        if start<0:
            start=0
        ans=0
        for i in range(start,min(n,limit)+1):
            upper=min(n-i,limit)
            lower=(n-i)-upper
            if lower<0:
                lower=0
            ans+=upper-lower+1
            # print(ans,i,upper,lower)
        return ans
        