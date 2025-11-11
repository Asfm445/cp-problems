# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

from collections import *

from collections import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums=list(set(nums))
        nums.sort()
        ans=set()
        print(nums)
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

            while left<right:
                s=nums[i]+nums[left]+nums[right]
                # print(s,i,left,right)
                if s==0:
                    ans.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif s>0:
                    right-=1
                else:
                    left+=1
        return [list(i) for i in ans]


            

        
        