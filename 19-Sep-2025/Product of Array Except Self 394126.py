# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prepro=[1]
        for i in nums:
            prepro.append(prepro[-1]*i)
        p2=[1]
        p3=[]
        for i in range(1,len(nums)+1):
            p2.append(p2[-1]*nums[-i])
        for i in range(len(nums)):
            p3.append(prepro[i]*p2[-i-2])
        return p3
        