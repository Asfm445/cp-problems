# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[nums[0]]
        for i in range(1,len(nums)):
            if i==1:
                memo.append(max(nums[0],nums[1]))
            else:
                # print(memo)
                memo.append(max(memo[i-1],nums[i]+memo[i-2]))
        return memo[-1]
        