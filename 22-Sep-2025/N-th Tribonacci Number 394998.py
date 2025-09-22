# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo=[0]
        for i in range(1,n+1):
            if i<3:
                memo.append(1)
            else:
                # print(i,memo)
                memo.append(memo[i-1]+memo[i-2]+memo[i-3])
        return memo[-1]
        