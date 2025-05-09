# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree=[0 for i in range(n)]
        finishTime=[time[i] for i in range(n)]
        graph=defaultdict(list)
        for u,v in relations:
            graph[u].append(v)
            indegree[v-1]+=1
        ans=0
        que=deque()
        for i in range(n):
            if indegree[i]==0:
                que.append(i+1)
        while que:
            p=que.popleft()
            for child in graph[p]:
                indegree[child-1]-=1
                finishTime[child-1]=max(finishTime[child-1],finishTime[p-1]+time[child-1])
                if indegree[child-1]==0:
                    que.append(child)
        return max(finishTime)

        
        