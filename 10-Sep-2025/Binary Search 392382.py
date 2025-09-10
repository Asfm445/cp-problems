# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1

        while a<=b:
            k=a+(b-a)//2
            if nums[k]==target:
                return k
            elif nums[k]<target:
                a=k+1
            elif nums[k]>target:
                b=k-1
        return -1