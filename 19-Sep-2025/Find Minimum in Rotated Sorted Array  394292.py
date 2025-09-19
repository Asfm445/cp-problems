# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min=nums[0]
        l=0
        r=len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>=min:
                l=m+1
            else:
                r=m-1
        if l>=len(nums):
            l=0
        return nums[l]