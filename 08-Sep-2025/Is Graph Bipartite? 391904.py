# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1 for _ in range(len(graph))]
        def dfs(node):
            for i in graph[node]:
                if color[i]==-1:
                    color[i]=1 if color[node]==0 else 0
                    # print(color[node],color[i],node,i)
                    if not dfs(i):
                        return False
                elif color[node]==color[i]:
                    return False
            return True
        for i in range(len(graph)):
            if color[i]==-1:
                color[i]==0
                if not dfs(i):
                    print(color)
                    return False
        return True


        