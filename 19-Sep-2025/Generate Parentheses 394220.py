# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def rec(open=1,close=1,st=''):
            if open>n and close>n:
                ans.append(st)
                return
            if open<=n:
                rec(open+1,close,st+'(')
            if close<=n and open>close:
                rec(open,close+1,st+')')
        rec()
        return ans
