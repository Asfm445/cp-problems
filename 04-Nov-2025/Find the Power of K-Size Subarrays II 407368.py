# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        a=0
        b=1
        f=0
        if len(nums)==1 or k==1:
            return nums
        while b<k-1:
            if nums[b]-nums[b-1]!=1:
                f+=1
            b+=1
        if nums[b]-nums[b-1]!=1:
            f+=1
        ans=[]
        # print(f)
        while b<len(nums):
            if f==0:
                ans.append(nums[b])
            else:
                print(f,a,b)
                ans.append(-1)

            if b==len(nums)-1:
                break
            
            if nums[b+1]-nums[b]!=1:
                f+=1
            b+=1
            if nums[a+1]-nums[a]!=1:
                f-=1
            a+=1
        else:
            if f==0:
                ans.append(nums[b])
            else:
                nums.append(-1)
        return ans
            

        