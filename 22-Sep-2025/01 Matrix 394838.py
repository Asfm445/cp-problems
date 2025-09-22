# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que=deque()
        ans=[[-1 for _ in range(len(mat[0]))] for _ in range(len(mat)) ]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    que.append((i,j))
                    ans[i][j]=0
        

        def inbound(i,j):
            return 0<=i<len(mat) and 0<=j<len(mat[0]) and ans[i][j]==-1
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
