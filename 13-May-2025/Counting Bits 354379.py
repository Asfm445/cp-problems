# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> list[int]:
        bitCounts = []
        for i in range(n + 1):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                print(i)
                i >>= 1
                print(i)
            bitCounts.append(count)
        return bitCounts
        