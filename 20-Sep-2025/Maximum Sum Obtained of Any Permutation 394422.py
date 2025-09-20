# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq=[0]*(len(nums)+1)
        mod=1e9+7
        for start, end in requests:
            freq[start]+=1
            freq[end+1]-=1
        sum=0
        for i, val in enumerate(freq):
            sum+=val
            freq[i]=sum
        freq=sorted(freq[:-1])
        nums.sort()
        ans=0
        i=1
        while i<=len(nums):
            ans+=freq[-i]*nums[-i] 
            ans%=mod
            i+=1
        return int(ans%mod)
        