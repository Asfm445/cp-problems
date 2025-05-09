# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans=[[0 for i in range(len(matrix[0]))]for _ in range(len(matrix))]
        def dfs(x,y,num=float('inf')):
            if not 0<=x<len(matrix) or not 0<=y<len(matrix[0]):
                return 0
            if matrix[x][y]>=num:
                return 0
            if ans[x][y]==0:
                ans[x][y]=1+max(dfs(x+1,y,matrix[x][y]),dfs(x-1,y,matrix[x][y]),dfs(x,y-1,matrix[x][y]),dfs(x,y+1,matrix[x][y]))
            return ans[x][y]
        mx=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx=max(dfs(i,j),mx)
        # print(ans)
        return mx
                
            

        
        
        