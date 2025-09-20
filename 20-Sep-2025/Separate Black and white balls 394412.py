# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        one_count=0
        ans=0
        for char in s:
            if char=="0":
                ans+=one_count
            else:
                one_count+=1
        return ans

        