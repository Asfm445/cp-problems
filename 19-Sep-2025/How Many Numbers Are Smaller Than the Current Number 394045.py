# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mx=max(nums)+1
        count_arr=[0]*(mx+1)
        for num in nums:
            count_arr[num]+=1
        pre_sum=[0]
        for num in count_arr:
            pre_sum.append(pre_sum[-1]+num)
        ans=[]
        for num in nums:
            ans.append(pre_sum[num])
        return ans
        