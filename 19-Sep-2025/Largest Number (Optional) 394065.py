# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

from typing import List

class Solution:
    def compare(self,num1,num2):
        return num1+num2>num2+num1

    def marge(self,arr1, arr2):
        a=0
        b=0
        ans=[]
        while a<len(arr1) and b<len(arr2):
            if self.compare(arr1[a],arr2[b]):
                ans.append(arr1[a])
                a+=1
            else:
                ans.append(arr2[b])
                b+=1
        ans.extend(arr1[a:])
        ans.extend(arr2[b:])
        return ans

    def rec(self,arr):
        if len(arr)<=1:
            return arr
        m=len(arr)//2
        left=self.rec(arr[:m])
        right=self.rec(arr[m:])

        return self.marge(left, right)

                
    def largestNumber(self, nums: List[int]) -> str:
        for i,num in enumerate(nums):
            nums[i]=str(num)
        arr=self.rec(nums)
        return str(int(''.join(arr)))