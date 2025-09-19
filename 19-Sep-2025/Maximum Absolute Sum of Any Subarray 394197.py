# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx=float("-inf")
        mn=float("inf")
        mx_sum=0
        mn_sum=0
        for num in nums:
            if mx_sum<0:
                mx_sum=0
            if mn_sum>0:
                mn_sum=0
            mx_sum+=num
            mn_sum+=num
            mx=max(mx,mx_sum)
            mn=min(mn,mn_sum)
        return max(mx,abs(mn))


        