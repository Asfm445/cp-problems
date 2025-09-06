# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]!=nums[i+1] !=nums[i+2]:
                return nums[i+1]
            elif i==0 and nums[i] !=nums[i+1]:
                return nums[0]
            elif i+2==len(nums)-1 and nums[i+1] !=nums[i+2]:
                return nums[i+2]
        if len(nums)==1:
            return nums[0]
