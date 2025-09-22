# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo=defaultdict(int)
        def rec(m,n):
            if min(m, n) < 0:
                memo[(m, n)] = 0
            elif m == 0 and n == 0:
                # print(memo,m,n)
                memo[(m, n)] = grid[m][n]
            if not (m, n) in memo:
                if m == 0:
                    memo[(m, n)] = rec(m, n - 1)+grid[m][n]
                elif n == 0:
                    memo[(m, n)] = rec(m - 1, n)+grid[m][n]
                else:
                    memo[(m, n)] = min(rec(m - 1, n) , rec(m, n - 1))+grid[m][n]
            # print(obstacleGrid[m - 1][n - 1])
            return memo[(m, n)] 
        m=len(grid)-1
        n=len(grid[0])-1
        ans=rec(m,n)
        # print(memo)
        return ans
        