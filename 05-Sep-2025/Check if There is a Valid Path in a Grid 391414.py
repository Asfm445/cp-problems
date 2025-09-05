# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution(object):
    def hasValidPath(self, grid):
        d={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(1,0),(0,1)],
            5:[(0,-1),(-1,0)],
            6:[(-1,0),(0,1)],
        }
        n,m=len(grid), len(grid[0])
        def check(x,y):
            if 0<=x<=n-1 and 0<=y<=m-1:
                return True
            return False
        memo=set()  
        stack=[]    
        def dfs(x=0,y=0, prev_x=None,prev_y=None):
            if (x,y) in memo:
                return False
            if not check(x,y):
                return False
            if prev_x is None and prev_y is None:
                prev_x,prev_y=d[grid[0][0]][0]
            ptr=grid[x][y]
            if (prev_x != x+d[ptr][0][0] or prev_y!=y+d[ptr][0][1] )and (prev_x != x+d[ptr][1][0] or prev_y!=y+d[ptr][1][1]):
        
                # print("prev is other",x,y,prev_x,prev_y)
                return False
            if x==n-1 and y==m-1:
                return True
            # print(d[ptr][1])
            memo.add((x,y))
            one=dfs(x+d[ptr][1][0], y+d[ptr][1][1], x,y)
            two=dfs(x+d[ptr][0][0], y+d[ptr][0][1], x,y)

            return one or two
        return dfs(0,0)
            
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        