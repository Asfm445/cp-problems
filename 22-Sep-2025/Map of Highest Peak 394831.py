# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que=deque()
        ans=[[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater)) ]

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]==1:
                    que.append((i,j))
                    ans[i][j]=0
        

        def inbound(i,j):
            return 0<=i<len(isWater) and 0<=j<len(isWater[0]) and ans[i][j]==-1
        dir=[(1,0),(0,1),(-1,0),(0,-1)]

        while que:
            n=len(que)
            for _ in range(n):
                i,j=que.popleft()
                for x,y in dir:
                    x+=i
                    y+=j
                    if inbound(x,y):
                        ans[x][y]=ans[i][j]+1
                        que.append((x,y))

        return ans


