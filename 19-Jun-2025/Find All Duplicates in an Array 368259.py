# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seeker=0
        while seeker<len(nums):
            holder=nums[seeker]-1
            if nums[seeker]!=nums[holder] :
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
            else:
                seeker+=1
        print(nums)
        return [nums[i] for i in range(len(nums)) if nums[i]-1!=i]
        # return nums