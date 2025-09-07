# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def inBound(row,clmn):
            if 0<=row<len(board) and 0<=clmn<len(board[0]):
                return True
            return False
        grid_memo=[[True for _ in range(len(board[0]))]for _ in range(len(board))]
        def dfs(i,j):
            if not inBound(i,j):
                return
            if board[i][j]!="O":
                return
            if not grid_memo[i][j]:
                return
            grid_memo[i][j]=False
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        i=0
        j=0
        while j<len(board[0]):
            dfs(i,j)
            j+=1
        j-=1
        i+=1
        while i<len(board):
            dfs(i,j)
            i+=1
        i-=1
        j-=1
        while j>=0:
            dfs(i,j)
            j-=1
        j+=1
        i-=1
        while i>=0:
            dfs(i,j)
            i-=1
        

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if grid_memo[i][j]:
                    board[i][j]="X"


        """
        Do not return anything, modify board in-place instead.
        """
        