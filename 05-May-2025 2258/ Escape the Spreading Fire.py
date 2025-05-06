from collections import deque
from copy import deepcopy
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions
        fireQueue = deque()  # Queue for fire starting points
        
        # Initialize the fire queue with all fire starting positions
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fireQueue.append((row, col, 1))

        def canEscape(waitTime):
            currentTime = 0
            simulationQueue = deque(fireQueue)  # Copy fire queue to avoid modifying the original
            visitedGrid = deepcopy(grid)

            def isValidCell(x, y):
                if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
                    return False
                if visitedGrid[x][y] == 3:
                    return -1  # Special case for visited grid cells
                return visitedGrid[x][y] == 0

            personAdded = False
            if not simulationQueue:
                simulationQueue.append((0, 0, -1))  # Add person to start position if fireQueue is empty
            
            while simulationQueue:
                queueSize = len(simulationQueue)

                if currentTime == waitTime:
                    personAdded = True
                    simulationQueue.append((0, 0, -1))  # Add person to queue after waiting

                for _ in range(queueSize):
                    x, y, entityType = simulationQueue.popleft()

                    if x == len(grid) - 1 and y == len(grid[0]) - 1:
                        # If the bottom-right corner is reached
                        if visitedGrid[x][y] == -1:
                            return currentTime
                        else:
                            return False

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if (isValidCell(nx, ny) is True or
                            (entityType == -1 and isValidCell(nx, ny) == -1)):
                            if (nx == len(grid) - 1 and ny == len(grid[0]) - 1 and entityType == 1):
                                simulationQueue.append((nx, ny, 3))
                                visitedGrid[nx][ny] = 3
                                continue
                            simulationQueue.append((nx, ny, entityType))
                            visitedGrid[nx][ny] = entityType

                if not personAdded and len(simulationQueue) == 0:
                    personAdded = True
                    simulationQueue.appendleft((0, 0, -1))

                currentTime += 1
            return False

        # Binary search to find the maximum waiting time
        left, right = 1, 10**9
        while left <= right:
            mid = (right + left) // 2
            if canEscape(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        result = canEscape(right)
        if result:
            return right
        return -1
