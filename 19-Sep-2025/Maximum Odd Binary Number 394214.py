# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ans=["0"]*len(s)
        ans[-1]="1"
        n=s.count("1")-1
        for i in range(n):
            ans[i]="1"
        return ''.join(ans)
        