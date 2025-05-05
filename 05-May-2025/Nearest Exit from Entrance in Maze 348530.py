# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inBound(x,y):
            if x==entrance[0] and y==entrance[1]:
                return False
            return  0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y]=='.' 
        que=deque()
        que.append((entrance[0],entrance[1],0))
        visited={(entrance[0],entrance[1])}
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        while que:
            x,y,dis=que.popleft()
            for u,v in directions:
                if inBound(x+u,y+v) and (x+u,y+v) not in visited:
                    if x+u==0 or y+v==0 or x+u==len(maze)-1 or y+v == len(maze[0])-1:
                        return dis+1
                    que.append((x+u,y+v,dis+1))
                    visited.add((x+u,y+v))
        return -1



        