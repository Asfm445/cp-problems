# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = defaultdict(list)
        s=set()
        for i in prerequisites:
            a, b = i
            course[a].append(b)
            s.add(a)
            s.add(b)
        l=[]
        for i in range(numCourses):
            if i not in s:
                l.append(i) 
        visited = set()
        que = []
        stack = set()
        can_done = [True]


        def top(v, visited, que):
            stack.add(v)
            for i in course[v]:
                if i not in visited:
                    if i in stack:
                        can_done[0] = False
                        print(can_done)
                        return False
                    top(i, visited, que)
            que.append(v)
            stack.remove(v)
            visited.add(v)


        for i in list(course):
            if i not in visited:
                top(i, visited, que)
        print(course)
        if can_done[0]:
            return l+que
        else:
            return []
        