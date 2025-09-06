# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution(object):
    def nextPermutation(self, nums):
        a=len(nums)-2
        while a>=0:
            if nums[a]<nums[a+1]:
                break
            a-=1
        left=a+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        if a>-1:
            elem=bisect_right(nums,nums[a],lo=a+1)
            if nums[elem]==nums[a]:
                elem+=1
            nums[elem],nums[a]=nums[a],nums[elem]
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        