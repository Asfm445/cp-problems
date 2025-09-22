# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    prev={1:1,2:2,3:3}
    def climbStairs(self, n: int) -> int:
        if n not in self.prev:
            self.prev[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.prev[n]

