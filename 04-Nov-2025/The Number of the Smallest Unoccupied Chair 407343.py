# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n=len(times)
        heap1=[]
        
        d={}
        def apply(i):
            d[i]=times[i]
            return i
        persons=[apply(i) for i in range(n)]
        heap2=[]
        persons.sort(key=lambda i:d[i])

        pl=0
        
        for i in persons:
            start,end=times[i]
            # print(heap2)
            while heap2 and heap2[0][0]<=start:
                heappush(heap1,heappop(heap2)[1])

            # print(heap2,heap1)

            if i==targetFriend:
                return heappop(heap1) if heap1 else pl
            
            
            if heap1:
                heappush(heap2,(end,heappop(heap1)))
            else:
                heappush(heap2,(end,pl))
                pl+=1



    
        