# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for i in range(len(equations)):
            a,b=equations[i]
            graph[a].append([b,values[i]])
            graph[b].append([a,1/values[i]])
        def dikestra(start,end):
            if not start in graph or not end in graph:
                return -1.0
            visited={start}
            stack=[start]
            shortpath=defaultdict(int)
            shortpath[start]=1
            while stack:
                p=stack.pop()
                if p==end:
                    return shortpath[end]
                for n,w in graph[p]:
                    if n in shortpath:
                        shortpath[n]=min(shortpath[p]*w,shortpath[n])
                    else:
                        shortpath[n]=shortpath[p]*w
                    if not n in visited:
                        stack.append(n)
                        visited.add(n)
            return -1.0
        ans=[]
        for a,b in queries:
            ans.append(dikestra(a,b))
        return ans

                



        