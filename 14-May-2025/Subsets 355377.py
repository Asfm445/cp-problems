# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**len(nums)):
            ans.append([])
            num=i
            n=0
            while num>0:
                if num&1:
                    ans[i].append(nums[n])
                num>>=1
                n+=1
        return ans
