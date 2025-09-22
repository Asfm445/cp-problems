# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0
        l=0
        ans=0
        for char in s:
            if char=="L":
                l+=1
            else:
                r+=1
            if l==r:
                ans+=1
                l=0
                r=0
        return ans


        