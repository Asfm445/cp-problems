# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

from collections import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        gragh = defaultdict(list)
        for i in times:
            a, b, c = i
            gragh[a].append([b, c])
        d = defaultdict(int)
        d[k] = 0
        visited = set()


        def findmin():
            mn = float("inf")
            mnv = None
            for i in d:
                if i not in visited:
                    if d[i] < mn:
                        mn = d[i]
                        mnv = i

            return mnv


        mx = 0
        while k:
            visited.add(k)
            for i in gragh[k]:
                if i[0] in d:
                    if d[i[0]] > d[k] + i[1]:
                        d[i[0]] = d[k] + i[1]
                else:
                    d[i[0]] = d[k] + i[1]
            k = findmin()

        if len(d)<n:
            return -1
        for i in d:
            mx=max(d[i],mx)
        return mx

        