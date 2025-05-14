# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        mx=max(start,goal)
        ans=0
        k=0
        while (1<<k)<=mx:
            if ((1<<k)&start ==0 or (1<<k)&goal==0) and not ((1<<k)&start ==0 and (1<<k)&goal==0):
                # print(k)
                ans+=1
            k+=1
        return ans

        