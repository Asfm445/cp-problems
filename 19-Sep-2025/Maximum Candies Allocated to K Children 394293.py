# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDivide(m):
            count=0
            for i in candies:
                count+=(i//m)
            if count>=k:
                return True
            else:
                return False
        left=1
        right=max(candies)
        while left<=right:
            md=left+(right-left)//2
            if canDivide(md):
                left=md+1
            else:
                right=md-1
        return left-1
