# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        most_lift=l

        while l<=r:
            m=l+(r-l)//2
            if nums[m]>=target:
                r=m-1
            else:
                l=m+1
        most_lift=l
        if not nums or l>=len(nums) or  nums[l]!=target:
            return [-1,-1]
        else:
            r=len(nums)-1
            while l<=r:
                m=l+(r-l)//2
                if nums[m]<=target:
                    l=m+1
                else:
                    r=m-1
            return [most_lift,r]
        