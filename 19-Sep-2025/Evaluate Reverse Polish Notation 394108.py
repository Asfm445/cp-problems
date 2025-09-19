# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in range(len(tokens)):
            if tokens[i]=='+':
                a=int(l.pop())+int(l.pop())
                l.append(a)
            elif tokens[i]=='-':
                a=int(l.pop())
                b=int(l.pop())
                l.append(b-a)
            elif tokens[i]=='*':
                a=int(l.pop())*int(l.pop())
                l.append(a)
            elif tokens[i]=='/':
                a=int(l.pop())
                b=int(l.pop())
                l.append(int(b/a))
            else:
                l.append(int(tokens[i]))
        for i in l:
            return i