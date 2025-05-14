# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def rec(choosed, i=0):
            if i >= len(nums):
                ans.append(choosed)
                return
            rec(choosed + [nums[i]], i + 1)
            rec(choosed, i + 1)


        rec([])
        return ans
        