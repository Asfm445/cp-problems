# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        counter=0
        for i,num in enumerate(nums):
            left=lower-num
            right=upper-num
            left_idx=bisect_left(nums,left,lo=i+1)
            right_idx=bisect_right(nums,right,lo=i+1)
            counter+=(right_idx-left_idx)
            # print(counter,left_idx,right_idx)
        return counter

        