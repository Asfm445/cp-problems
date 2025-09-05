# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution(object):
    def getOrder(self, tasks):
        heap=[]
        ans=[]
        sorted_tasks=[[task[0],task[1],i]for i,task in enumerate(tasks)]
        sorted_tasks.sort(key=lambda x:x[0])
        i=0
        while i<len(tasks):
            time=sorted_tasks[i][0]
            while i<len(tasks) and sorted_tasks[i][0]<=time:
                heapq.heappush(heap,(sorted_tasks[i][1],sorted_tasks[i][2]))
                i+=1
            # print(heap,i)
            while heap:
                process,task=heapq.heappop(heap)
                ans.append(task)
                time+=process
                while i<len(tasks) and sorted_tasks[i][0]<=time:
                    heapq.heappush(heap,(sorted_tasks[i][1],sorted_tasks[i][2]))
                    i+=1
        return ans


        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        