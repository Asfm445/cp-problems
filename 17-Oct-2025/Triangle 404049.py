# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo=defaultdict(int)
        def rec(i,j):
            if i>=len(triangle):
                return 0
            mn=float('inf')
            if (i,j) not in memo:
                memo[(i,j)]=min(rec(i+1,j)+triangle[i][j],rec(i+1,j+1)+triangle[i][j])
            return memo[(i,j)]
        ans=rec(0,0)
        # print(memo)
        return ans
        