# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        que=[1,2,3,4,5,6,7,8,9]
        s=set()
        ans=[]
        now=None
        l=[]
        for i in pattern:
            if i!=now:
                l.append(i)
                l.append(1)
                now=i
            else:
                l[-1]+=1
        st=1
        ptr=0
        while st<len(l):
            sm=que[ptr]
            if l[st-1]=="I":
                ptr+=1
                ans.append(str(sm))
                l[st]-=1
            elif l[st-1]=="D":
                ans.append(str(sm+l[st]))
                que.remove(sm+l[st])
                l[st]-=1
            if l[st]<=0:
                st+=2
        ans.append(str(que[ptr]))
        return ''.join(ans)




        