# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution(object):
    def longestNiceSubarray(self, nums):
        a=0
        b=1
        sum=nums[0]
        mx=1
        while b<len(nums):
            if sum&nums[b]!=0:
                mx=max(mx,b-a)
                if a+1==b:
                    sum=nums[b]
                    a=b
                    b+=1
                else:
                    sum-=nums[a]
                    a+=1
            else:
                sum+=nums[b]
                b+=1
        mx=max(b-a,mx)
        return mx
        """
        :type nums: List[int]
        :rtype: int
        """
        