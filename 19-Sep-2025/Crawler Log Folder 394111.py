# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s='../'
        t="./"
        a=0
        for i in logs:
            if i==s:
                if a==0:
                    continue
                else:
                    a-=1
            elif i==t:
                continue
            else:
                a+=1
        if a<=0:
            return 0
        else:
            return a