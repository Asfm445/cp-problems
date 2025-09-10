# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result={}
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                result[nums2[stack.pop()]]=nums2[i]
            stack.append(i)
        ans=[]
        for i in nums1:
            if i in result:
                ans.append(result[i])
            else:
                ans.append(-1)
        return ans