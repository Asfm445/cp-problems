# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d=defaultdict(int)
        def pop(e):
            if d[e]>1:
                d[e]-=1
            else:
                d.pop(e)
        for i in arr:
            if i%k==0:
                if 0 in d:
                    pop(0)
                else:
                    d[0]+=1
            else:
                if k-i%k in d:
                    pop(k-i%k)
                else:
                    d[i%k]+=1
        if d:
            return False
        return True
        