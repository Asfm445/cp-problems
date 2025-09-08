# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E


from collections import defaultdict

class UnionFind:
    def __init__(self,n):
        self.root =defaultdict(int)
        self.size= defaultdict(lambda : 1)
    def find(self, X):
        if X not in self.root:
            self.root[X]=X
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

        
n,m=map(int,input().split())

degree=defaultdict(lambda : 0)
uf=UnionFind(n)
for _ in range(m):
    node1,node2 = map(int,input().split())
    uf.union(node1, node2)
    degree[node1]+=1
    degree[node2]+=1

s=set()
# print(degree)
for i in uf.root:
    s.add(uf.find(i))
# print(s)
for i in uf.root:
    root=uf.find(i)
    
    if degree[i]!=2 and root in s:
        s.remove(root)
    # print(s,i)
print(len(s))
    
