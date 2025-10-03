# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        # print(math.log2(10**6)*100*100)

        if len(heights)==1 and  len(heights[0])==1:
            return 0

        mx=0
        mn=float("inf")
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(x,y):
            return 0<=x<len(heights) and 0<=y<len(heights[0])


        for i in range(len(heights)):
            for j in range(len(heights[0])):
                for x_dr, y_dr in dirs:
                    # print(i,j,i+x_dr,j+y_dr, inbound(i+x_dr, j+ y_dr))
                    if inbound(i+x_dr, j+ y_dr):
                        mn=min(mn,math.fabs(heights[i][j]-heights[i+x_dr][j+y_dr]))
                        mx=max(mx,math.fabs(heights[i][j]-heights[i+x_dr][j+y_dr]))
        mn=int(mn)
        mx=int(mx)

        def bfs(k):
            visited = [[False] * len(heights[0]) for _ in range(len(heights))]
            que = deque()
            que.append((0, 0))
            visited[0][0] = True  # MARK WHEN ADDING TO QUEUE

            while que:
                x, y = que.popleft()
                # visited[x][y] = True  # REMOVE THIS LINE - too late!
                
                if x == len(heights)-1 and y == len(heights[0])-1:
                    return True
                    
                for x_dr, y_dr in dirs:
                    cur_x, cur_y = x + x_dr, y + y_dr
                    if inbound(cur_x, cur_y) and not visited[cur_x][cur_y]:
                        if abs(heights[cur_x][cur_y] - heights[x][y]) <= k:
                            visited[cur_x][cur_y] = True  # MARK WHEN ADDING
                            que.append((cur_x, cur_y))
            
            return False
        ans=mx
        # print(mx,mn)
        while mn<=mx:
            md=(mn+mx)//2
        
            if bfs(md):
                ans=md
                mx=md-1
            else:
                mn=md+1
        return int(ans)
            
        