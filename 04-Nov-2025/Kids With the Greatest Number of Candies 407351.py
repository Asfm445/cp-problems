# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        mx=max(candies)
        ans=[False for _ in range(len(candies))]

        for i,val in enumerate(candies):
            cur=val+extraCandies
            if cur>=mx:
                ans[i]=True
        return ans

        