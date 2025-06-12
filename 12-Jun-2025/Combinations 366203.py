# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def rec(arr,i=1):
            if len(arr)==k:
                ans.append(arr)
                return
            if i>n:
                return
            rec(arr+[i],i+1)
            rec(arr,i+1)
        rec([])
        return ans
        