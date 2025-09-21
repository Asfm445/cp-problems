# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap=[]
        for i, arr in enumerate(grid):
            arr.sort()
            for i in range(1,limits[i]+1):
                heapq.heappush(heap,arr[-i])
                if len(heap)>k:
                    heapq.heappop(heap)
        return sum(heap)
        