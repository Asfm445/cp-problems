# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def canFormTriangle(self,s1,s2,s3):
        if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
            return s1+s2+s3
        return False
    def largestPerimeter(self, nums: List[int]) -> int:
        a=0
        b=1
        c=2
        mx=0
        nums.sort()
        while c<len(nums):
            p=self.canFormTriangle(nums[a],nums[b],nums[c])
            if p:
                mx=max(p,mx)
            a+=1
            b+=1
            c+=1
        return mx

        