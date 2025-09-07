# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        a=0
        b=1
        while b<len(nums):
            if nums[a]==nums[b]:
                nums[a]=2*nums[a]
                nums[b]=0
                a+=1
                b+=1
            a+=1
            b+=1
        r=0
        l=0
        while r<len(nums):
            if nums[r]!=0:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
            r+=1
        return nums

        