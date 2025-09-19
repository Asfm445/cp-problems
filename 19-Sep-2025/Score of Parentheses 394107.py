# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                s = 0
                while stack and stack[-1] != "(":
                    s += stack.pop()
                else:
                    stack.pop()
                    if s > 0:
                        stack.append(2 * s)
                    else:
                        stack.append(1)
        return sum(stack)