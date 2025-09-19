# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        r=len(citations)-1

        le=len(citations)

        while l<=r:
            m=l+(r-l)//2
            if citations[m]>=le-m:
                r=m-1
            else:
                l=m+1
        print(l)
        return le-l