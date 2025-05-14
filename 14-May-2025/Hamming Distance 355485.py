# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(x >> i & 1 != y >> i & 1 for i in range(32))
        