# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution(object):
    def xorAllNums(self, nums1, nums2):
        xor_nums2=0
        for num in nums2:
            xor_nums2^=num
        ans=0
        for num in nums1:
            if len(nums2)%2==0:
                ans^=xor_nums2
            else:
                ans^=xor_nums2^num
        return ans
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        