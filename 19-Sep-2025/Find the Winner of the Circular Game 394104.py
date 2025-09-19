# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        if k==1:
            return n
        for i in range(1,n+1):
            l.append(i)

        def func(n,k,k2):
            if len(n)==1:
                return n[0]
            if k==0 :
                k=k2
                print(k)
            if k>len(n):
                if k%len(n)==0:
                    k=len(n)
                else:
                    k%=len(n)
                    
            # if k%len(n)==0:
            #     return n

            l=[]
            i=0
            while i<len(n):
                if i!=k-1:
                    l.append(n[i])
                else:
                    k+=k2
                i+=1
            else:
                k=k-len(n)
                print(k)
            return func(l,k,k2)
        return func(l,k,k)

