# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    memo={0:0,1:1}
    def fib(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n]=self.fib(n-1)+self.fib(n-2)
        return self.memo[n]


        