# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        l=[]
        for i in range(n):
            if i==0 or i==1:
                l.append(False)
            else:
                l.append(True)
        d=2
        while d*d<=n:
            s=d*d
            while s<n:
                l[s]=False
                s+=d
            d+=1
        return l.count(True)
    

        