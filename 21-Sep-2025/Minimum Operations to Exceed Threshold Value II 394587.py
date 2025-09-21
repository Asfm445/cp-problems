# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans=0
        while len(nums)>=2 and  nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)

            heapq.heappush(nums,x*2+y)
            ans+=1
        return ans
        