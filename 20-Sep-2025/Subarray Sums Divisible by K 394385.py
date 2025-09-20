# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum=0
        d=defaultdict(int)
        d[0]=1
        ans=0
        for i in nums:
            sum+=i
            val=sum%k
            ans+=d[val]
            d[val]+=1
        return ans
        