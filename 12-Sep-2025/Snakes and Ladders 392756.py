# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        visited = [False] * (target + 1)  # Track if a cell has been visited
        que = deque()
        que.append((1, 0))  # (current_cell, moves)
        visited[1] = True
        
        def get_coord(p):
            # Convert a 1-based cell number to (x, y) coordinates
            p_zero = p - 1
            r = p_zero // n
            x = n - 1 - r  # Invert the row: top row is 0, bottom is n-1
            offset = p_zero % n
            if r % 2 == 0:
                y = offset
            else:
                y = n - 1 - offset
            return x, y
        
        while que:
            curr, moves = que.popleft()
            if curr == target:
                return moves
                
            # Roll the die: from curr+1 to curr+6
            for next_cell in range(curr + 1, min(curr + 7, target + 1)):
                x, y = get_coord(next_cell)
                # Check if the cell has a ladder/snake
                if board[x][y] != -1:
                    final_cell = board[x][y]
                else:
                    final_cell = next_cell
                    
                # If we haven't visited the final cell, add it to the queue
                if not visited[final_cell]:
                    visited[final_cell] = True
                    que.append((final_cell, moves + 1))
                    
        return -1