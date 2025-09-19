# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=[nums.count(0),nums.count(1),nums.count(2)]
        a=0
        for i in range(len(nums)):
            while count[a]<=0:
                a+=1
        
            nums[i]=a
            count[a]-=1

        """
        Do not return anything, modify nums in-place instead.
        """
        