# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color=[-1]*len(graph)
        ans=[]
        def dfs(node):
            if color[node]==1:
                return True
            if color[node]==0:
                return False
            color[node]=0
            for child in graph[node]:
                if not dfs(child):
                    return False
            color[node]=1
            ans.append(node)
            return True
        for i in range(len(graph)):
            dfs(i)
        return sorted(ans)