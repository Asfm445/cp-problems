# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        bool=False
        stack=[]
        string,num='',0
        for i in s:
            if i=='[':
                stack.append(string)
                stack.append(num)
                string,num='',0
            elif i==']':
                n1=stack.pop()
                str2=stack.pop()

                string=str2+string*n1
            elif i.isdigit():
                num=num*10+int(i)
            else:
                string+=i
            print(stack)
        print(string)
        return string
        
        