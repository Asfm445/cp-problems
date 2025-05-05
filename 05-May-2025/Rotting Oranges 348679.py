# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que=deque()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        fresh=0
        def inBound(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    que.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        ans=0
        while que and fresh>0:
            for _ in range(len(que)):
                i,j=que.popleft()
                for k,m in directions:
                    if inBound(i+k,j+m) and grid[i+k][j+m]==1:
                        grid[i+k][j+m]=2
                        fresh-=1
                        que.append((i+k,j+m))
            ans+=1
        return ans if fresh==0 else -1



        