# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        memo={}

        def rec(i,j,sum=None):
            if i>=j:
                return 0
            mx=0
            if (i,j,sum) not in memo:
                if sum is None:
                    return 1+max(rec(i+2,j,nums[i]+nums[i+1]),rec(i+1,j-1,nums[i]+nums[j]),rec(i,j-2,nums[j-1]+nums[j]))
                
                if nums[i]+nums[i+1]==sum:
                    mx=max(rec(i+2,j,nums[i]+nums[i+1])+1,mx)
                if nums[i]+nums[j]==sum:
                    mx=max(rec(i+1,j-1,nums[i]+nums[j])+1,mx)
                if nums[j-1]+nums[j]==sum:
                    mx=max(rec(i,j-2,nums[j-1]+nums[j])+1,mx)
                # print(i,j,sum,mx+1)
                memo[(i,j,sum)]= mx
            return memo[(i,j,sum)]
        ans=rec(0,len(nums)-1)
        # print(memo)
        return ans




        