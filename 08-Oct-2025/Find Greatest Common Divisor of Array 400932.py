# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)

        ans=math.gcd(mx,mn)
        return ans
        