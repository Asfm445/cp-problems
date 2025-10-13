# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo={}

        def rec(target):
            if target==0:
                return 1
            if target<0:
                return 0
            if target not in memo:
                ans=0
                for i in nums:
                    ans+=rec(target-i)
                memo[target]=ans
            return memo[target]
        return rec(target)
            
        