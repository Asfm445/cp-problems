# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s1)
        a=0
        b=0
        while b<len(s2):
            if s2[b] in d:
                d[s2[b]]-=1
                if d[s2[b]]==0:
                    d.pop(s2[b])
                if len(d)==0:
                    return True
                b+=1
            else:
                if a==b:
                    a+=1
                    b+=1
                else:
                    d[s2[a]]+=1
                    a+=1
        return False


        