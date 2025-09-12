# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        que=deque()
        graph=defaultdict(list)
        degree=[0]*n
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            degree[n1]+=1
            degree[n2]+=1

        for i,deg in enumerate(degree):
            if deg<=1:
                que.append(i)
        remaining=n
        while remaining>2:
            leaves=len(que)
            remaining-=leaves
            for _ in range(leaves):
                node=que.popleft()
                for child in graph[node]:
                    degree[child]-=1
                    if degree[child]==1:
                        que.append(child)
        return list(que)


        