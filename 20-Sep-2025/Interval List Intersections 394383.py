# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a=0
        b=0
        ans=[]
        while a<len(firstList) and b<len(secondList):
            start1,end1=firstList[a]
            start2,end2=secondList[b]
            if end1<=end2:
                if end1>=start2:
                    ans.append([max(start1,start2),end1])
                a+=1
            else:
                if end2>=start1:
                    ans.append([max(start1,start2),end2])
                b+=1
        return ans

        