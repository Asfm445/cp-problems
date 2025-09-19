# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seeker=0
        while seeker<len(nums):
            holder=nums[seeker]-1
            if nums[seeker]!=nums[holder] :
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
            else:
                seeker+=1
        for i in range(len(nums)):
            if nums[i]-1!=i:
                return [nums[i],i+1]

        # return [i+1,nums[i] for i in range(len(nums)) if ]