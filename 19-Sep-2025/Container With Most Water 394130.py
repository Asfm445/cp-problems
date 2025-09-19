# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx=0
        a=0
        b=len(height)-1
        while a<b:
            area=min(height[a],height[b])*(b-a)
            mx=max(area,mx)
            if height[a]<=height[b]:
                a+=1
            else:
                b-=1
        return mx

        