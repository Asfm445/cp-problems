# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]==1:
            return -1
        grid[0][0]=1
        que=deque()
        que.append((0,0,1))
        def inBound(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==0
        directions=[(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        while que:
            i,j,val=que.popleft()
            # print(que)
            for l,k in directions:
                if inBound(i+l,j+k):
                    grid[i+l][j+k]=val+1
                    que.append((i+l,j+k,val+1))
            # print(grid,i,j)
        ans=grid[len(grid)-1][len(grid[0])-1]
        # print(grid)
        return ans if ans>0 else -1

        