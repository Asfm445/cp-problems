# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k>len(nums):
            k-=len(nums)
        a=-k
        for i in range(k):
            nums.insert(i,nums[a])
            nums.pop(a)
            a+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        