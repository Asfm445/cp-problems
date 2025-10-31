# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        s=0
        d={}
        ans=float("inf")
        d[0]=-1
        tot=sum(nums)
        if tot<p:
            return -1
        k=tot%p
        for i,num in enumerate(nums):
            num%=p
            # print(p-num)
            s=(s+num)%p
            if s<k:
                find=p+s-k
                print("here",i)
            else:
                print("hdsfgdhj",i)
                find=s-k
            d[s]=i
            # if i==6:
            #     print(d)
            if find in d:
                # print(i,d[find],find)
                ans=min(ans,i-d[find])
        #     print(ans)
        # print(d,k)
        return ans if ans<float("inf") and ans<len(nums) else -1
        