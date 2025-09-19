# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path2=[]
        for i in path.split('/'):
            if len(i)==0:
                continue
            elif i=='..' :
                if path2:
                    path2.pop()
            elif i=='.':
                continue
            else:
                path2.append(i)
        return '/'+'/'.join(path2) 