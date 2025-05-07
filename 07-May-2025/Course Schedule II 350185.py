# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree=[0 for i in range(numCourses)]
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            inDegree[a]+=1
        que=deque()
        visited=set()
        ans=[]
        for i in range(numCourses):
            if inDegree[i]==0:
                que.append(i)
        while que:
            p=que.popleft()
            ans.append(p)
            for i in graph[p]:
                inDegree[i]-=1
                if inDegree[i]==0:
                    que.append(i)
        if len(ans)<numCourses:
            return []
        else:
            return ans

       
        