# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pro=defaultdict(int)
        ans=0
        for i in range(len(nums)):
            for j in range(i):
                pr=nums[i]*nums[j]
                ans+=pro[pr]*8
                pro[pr]+=1
        return ans
        