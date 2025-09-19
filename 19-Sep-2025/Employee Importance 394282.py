# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(int)
        for i in employees:
            graph[i.id]=i

        def dfs(id):
            sum=graph[id].importance
            for i in graph[id].subordinates:
                sum+=dfs(i) 
            return sum
        return dfs(id)
        