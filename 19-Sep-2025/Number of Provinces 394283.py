# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected : List[List[int]]) -> int:
        parent=[i for i in range(len(isConnected))]
        size=[1 for i in range(len(isConnected))]

        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return find(parent[x])
        def union(x,y):
            r_x=find(x)
            r_y=find(y)
            if r_y!=r_x:
                if size[r_x]<size[r_y]:
                    parent[r_x]=r_y
                    size[r_y]+=r_x
                else:
                    parent[r_y]=r_x
                    size[r_x]+=r_y
        ans=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and find(i)!=find(j):
                    union(i,j)
                    ans-=1
        return ans



        
        