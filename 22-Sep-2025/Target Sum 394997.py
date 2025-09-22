# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(list)


        def fn(sum=target, ptr=0):
            if ptr >= len(nums):
                if sum == 0:
                    return [True, 1]
                else:
                    return [False, 0]
            if not (sum, ptr) in memo:
                left = fn(sum - nums[ptr], ptr + 1)
                right = fn(sum + nums[ptr], ptr + 1)
                ans = 0
                print(sum, ptr, left, right)
                if left[0] or right[0]:
                    ans = left[1] + right[1]
                memo[(sum, ptr)] = [left[0] or right[0], ans]
            return memo[(sum, ptr)]
        return fn()[1]

                

        