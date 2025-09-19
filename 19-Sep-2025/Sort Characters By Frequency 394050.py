# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import *
class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(list)
        d1=defaultdict(int)
        st=''
        l=[]
        for i in s:
            d1[i]+=1
        for i in d1:
            d[d1[i]].append(i)
            l.append(d1[i])
        l.sort(reverse=True)
        print(d)
        s=set()
        for i in l:
            if not i in s:
                for j in d[i]:
                    st+=j*i
            s.add(i)
        return st
        