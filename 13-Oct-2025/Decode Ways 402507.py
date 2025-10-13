# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:


        memo={}
        
        def rec(i):

            if i>=len(s):
                return 1
            if s[i]=="0":
                return 0
            if i==len(s)-1:
                return 1

            ans=0
            if i not in memo:
                if int(s[i]+s[i+1])<=26:
                    ans+=rec(i+2)
                if s[i+1]!="0":
                    ans+=rec(i+1)
                memo[i]=ans
            return memo[i]

            
            
        return rec(0)
            
            
        