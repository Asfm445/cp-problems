# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans=[1]*len(nums)
        for i in range(1, len(nums)):
            subproblems = [ans[k] for k in range(i) if nums[k] < nums[i]]
            ans[i] = max(subproblems, default=0)
            ans[i] +=1
        return max(ans)