# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d1=defaultdict(int)
        d2=Counter(s)
        d1[s[0]]+=1
        a=0
        b=1
        ans=[]
        def drop(d,e):
            d[e]-=1
            if d[e]<=0:
                d.pop(e)
        drop(d2,s[0])
        while b<len(s):
            # print(d1,d2)
            if d1.keys().isdisjoint(d2.keys()):
                print(s[a:b])
                ans.append(b-a)
                a=b
                d1=defaultdict(int)
            d1[s[b]]+=1
            drop(d2,s[b])
            b+=1
        ans.append(b-a)
        return ans


        