# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        def toStack(stack1,s):
            for i in s:
                if i=='#':
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(i)
        toStack(stack1,s)
        toStack(stack2,t)
        if stack1==stack2:
            return True
        return False
        


        