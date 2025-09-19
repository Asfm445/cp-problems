# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(i,j):
            if not 0<=i<len(grid) or not  0<=j< len(grid[i]):
                return 0
            if visited[i][j] or grid[i][j]==0:
                return 0
            visited[i][j]=True
            return 1+dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)
            
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans=max(ans,dfs(i,j))
        return ans
        