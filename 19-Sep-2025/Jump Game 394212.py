# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a=0
        if len(nums)<=1:
            return True
        while a<len(nums):
            if a==len(nums)-1:
                return True
            if nums[a]==0:
                return False
            mx=nums[a+1]
            i=a+1
            j=a+2
            while j<=a+nums[a]:
                if j>=len(nums)-1:
                    return True
                if nums[j]+(j-i)>mx and nums[j]>0:
                    mx=nums[j]
                    i=j
                j+=1
            a=i

           
        return False

        