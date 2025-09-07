# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph=defaultdict(list)
        for i,head in enumerate(manager):
            if head!=-1:
                graph[head].append(i)
        def dfs(head):
            mx=0
            for emp in graph[head]:
                mx=max(mx,dfs(emp))
            return mx+informTime[head]
        return dfs(headID)
                
        