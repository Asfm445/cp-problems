# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(1,n+1)]
        self.size=[1 for i in range(1,n+1)]
    def find(self,x):
        if self.parent[x-1]==x:
            return x
        self.parent[x-1]=self.find(self.parent[x-1])
        return self.find(self.parent[x-1])
    def union(self,x,y):
        r_x=self.find(x)
        r_y=self.find(y)
        if r_y!=r_x:
            if self.size[r_x-1]<self.size[r_y-1]:
                self.parent[r_x-1]=r_y
                self.size[r_y-1]+=self.size[r_x-1]
            else:
                self.parent[r_y-1]=r_x
                self.size[r_x-1]+=self.size[r_y-1]
        #     return True
        # return False

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # parent=[i for i in range(len(stones))]
        uf=UnionFind(len(stones))
        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    uf.union(i,j)
        s=set()
        for i in range(len(stones)):
            s.add(uf.find(i))
        return len(stones)- len(s)
                    

            


        