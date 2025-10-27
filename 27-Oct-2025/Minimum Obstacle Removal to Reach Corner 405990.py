# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        n,m=len(grid), len(grid[0])

        dis=[[float("inf") for _ in range(m)] for _ in range(n)]

        heap=[(0,(0,0))]
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        def in_bound(x,y):
            return 0<=x<n and 0<=y<m
        dis[0][0]=grid[0][0]

        while heap:
            node_dis, (i,j)=heappop(heap)

            for x,y in dir:
                nx,ny=x+i,y+j
                if in_bound(nx,ny):
                    if dis[nx][ny]>node_dis+grid[nx][ny]:
                        heappush(heap,(node_dis+grid[nx][ny],(nx,ny)))
                        dis[nx][ny]=node_dis+grid[nx][ny]
        print(dis)
        return dis[n-1][m-1] if dis[n-1][m-1]<float("inf") else -1