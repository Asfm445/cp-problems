# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        que=deque()
        que.append((sr,sc))

        org=image[sr][sc]

        if org==color:
            return image

        dir=[(1,0),(0,1),(-1,0),(0, -1)]

        def inbound(x,y):
            return 0<=x<len(image) and 0<=y<len(image[0]) and image[x][y]==org

        while que:
            i,j=que.popleft()
            image[i][j]=color
            for x,y in dir:
                x+=i
                y+=j
                if inbound(x,y):
                    que.append((x,y))

        return image
        