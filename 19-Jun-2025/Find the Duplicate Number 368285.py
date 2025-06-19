# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seeker=0
        while seeker<len(nums):
            holder=nums[seeker]-1
            if nums[seeker]!=nums[holder] :
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
            else:
                seeker+=1
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return nums[i]