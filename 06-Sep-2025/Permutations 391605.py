# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def rec(arr, left):
            if len(arr) == len(nums):
                ans.append(arr)
                return
            for j in range(len(left)):
                rec(arr + [left[j]], left[:j] + left[j + 1 :])


        rec([], nums[:])
        return ans