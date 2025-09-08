# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

from typing import List

class UnionFind:
    def __init__(self,n):
        self.root =[i for i in range(n)]
        self.size= [1]*n
    def find(self, X):
        if X == self.root[X]:
            return X
        self.root[X]=self.find(self.root[X])
        return self.find(self.root[X])
    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)
        if rootX!=rootY:
            if self.size[rootX]<=self.size[rootY]:
                self.root[rootX]=rootY
                self.size[rootY]+=self.size[rootX]
            elif self.size[rootX]>self.size[rootY]:
                self.root[rootY]=rootX
                self.size[rootX]+=self.size[rootY]

        

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        degree=[0]*n
        uf=UnionFind(n)
        for node1,node2 in edges:
            uf.union(node1, node2)
            degree[node1]+=1
            degree[node2]+=1

        s=set()
        for i in range(n):
            s.add(uf.find(i))
        for i in range(n):
            root=uf.find(i)
            if (degree[i]!=degree[root] or degree[i]!=uf.size[root]-1)and root in s:
                s.remove(root)
        return len(s)
    