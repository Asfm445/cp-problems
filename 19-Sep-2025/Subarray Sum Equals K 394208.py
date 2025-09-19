# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l=[0]
        count=0
        def add(a,d):
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        sum=0
        d={}
        for i in nums:
            sum+=i
            if sum==k:
                count+=1
            if sum-k in d:
                count+=d[sum-k]
            add(sum,d)
        return count
        
        