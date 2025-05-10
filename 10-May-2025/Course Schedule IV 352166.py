# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq=defaultdict(set)
        indegree=[0]*numCourses
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        que=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                que.append(i)
        while que:
            p=que.popleft()
            for child in graph[p]:
                prereq[child].add(p)
                for i in prereq[p]:
                    prereq[child].add(i)
                indegree[child]-=1
                if indegree[child]==0:
                    que.append(child)
        ans=[]
        for u,v in queries:
            ans.append(u in prereq[v])
        # print(prereq)
        return ans
                


        