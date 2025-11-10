# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph=defaultdict(list)
        print(len(dislikes))
        # print(graph)

        for per1,per2 in dislikes:
            graph[per1].append(per2)
            graph[per2].append(per1)

        print(graph)

        color=[0]*(n+1)

        def dfs(node):
            ans=True
            for child in graph[node]:
                if color[child]==color[node]:
                    print(child,node)
                    return False
                elif color[child]==0:
                    color[child]=-color[node]
                    ans=dfs(child) and ans

            return ans
        ans=True
        keys=list(graph.keys())
        for node in keys:
            
            if color[node]==0:
                color[node]=1
                ans= ans and dfs(node)
        return ans
        
                
                
        