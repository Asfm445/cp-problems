# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution(object):
    def xorQueries(self, arr, queries):
        pre_xor=[0]
        for num in arr:
            pre_xor.append(pre_xor[-1]^num)
        ans=[]
        for left,right in queries:
            ans.append(pre_xor[right+1]^pre_xor[left])
        return ans
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        