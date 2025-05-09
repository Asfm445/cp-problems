# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0 for i in range(len(quiet))]
        ans=[i for i in range(len(quiet))]
        for u,v in richer:
            graph[u].append(v)
            indegree[v]+=1
        que=deque()
        for i in range(len(quiet)):
            if indegree[i]==0:
                que.append(i)
        while que:
            p=que.popleft()
            for i in graph[p]:
                if quiet[ans[p]]<quiet[ans[i]]:
                    ans[i]=ans[p]
                indegree[i]-=1
                if indegree[i]==0:
                    que.append(i)
        return ans
