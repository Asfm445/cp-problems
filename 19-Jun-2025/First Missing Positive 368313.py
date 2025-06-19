# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seeker=0
        nums=list(set(nums))
        while seeker<len(nums):
            holder=nums[seeker]-1
            if holder<0 or holder>=len(nums):
                nums[seeker],nums[-1]=nums[-1],nums[seeker]
                seeker+=1
            elif nums[seeker]!=nums[holder] :
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
            else:
                seeker+=1
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return i+1
        return max(nums)+1
        