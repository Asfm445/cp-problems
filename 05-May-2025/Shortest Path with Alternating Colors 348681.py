# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        red=1
        blue=-1
        for v1,v2 in redEdges:
            graph[v1].append([v2,red])
        for v1,v2 in blueEdges:
            graph[v1].append([v2,blue])
        ans=[-1 for i in range(n)]
        que=deque()
        que.append([0,0,0])
        ans[0]=0
        visited={(0,0)}
        while que:
            node,dis,prevColor=que.popleft()
            for child,color in graph[node]:
                if (child,color) not in visited and color!=prevColor:
                    if ans[child]==-1:
                        ans[child]=dis+1
                    que.append([child,dis+1,color])
                    visited.add((child,color))
        return ans


        