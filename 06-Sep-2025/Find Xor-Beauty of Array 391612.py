# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution(object):
    def xorBeauty(self, nums):
        ans=0
        for num in nums:
            ans^=num
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        