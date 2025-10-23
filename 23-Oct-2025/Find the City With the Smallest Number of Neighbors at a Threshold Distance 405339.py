# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis=[[float("inf") for _ in range(n)]for _ in range(n)]

        for i in range(n):
            dis[i][i]=0
        
        for n1,n2, w in edges:
            dis[n1][n2]=w
            dis[n2][n1]=w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
        
        ans=0
        mn=float("inf")
        for i in range(n):
            c=0
            for j in range(n):
                if i!=j and dis[i][j]<=distanceThreshold:
                    c+=1
            # print(c,i,mn)
            if c<=mn:
                mn=c
                ans=i
        return ans
        