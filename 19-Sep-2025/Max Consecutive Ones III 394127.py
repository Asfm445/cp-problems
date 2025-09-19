# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        a=0
        b=0
        max=0
        while b<len(nums):
            if k>=0:
                if nums[b]==1:
                    b+=1
                else:
                    b+=1
                    k-=1
            else:
                # a+=1
                if b-1-a>max:
                    max=b-1-a
                # print(max)
                if nums[a]==1:
                    a+=1
                else:
                    k+=1
                    a+=1
        if k<0:
            a+=1
        if len(nums)-a>max:
            max=len(nums)-a
        # print(a,b)
        return max
        