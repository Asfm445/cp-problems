# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans=[[]for i in range(n)]
        graph=defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
        def dfs(node):
            if ans[node]:
                return ans[node]+[node]
            for parent in graph[node]:
                for i in dfs(parent):
                    if not i in ans[node]:
                        ans[node].append(i)
                ans[node].sort()
            return ans[node]+[node]
        for i in range(n):
            dfs(i)
        return ans
        