# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1 for i in range(n+1)]

    def find(self, x):
        if self.parent[x]==x:
            return x

        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    
    
    def union(self,x,y):
        p_x=self.find(x)
        p_y=self.find(y)

        if p_x!=p_y:
            if self.size[p_x]>=self.size[p_y]:
                self.parent[p_y]=p_x
                self.size[p_x]+=self.size[p_y]
            else:
                self.parent[p_x]=p_y
                self.size[p_y]+=self.size[p_x]


n,m=map(int,input().split())
uf=UnionFind(n)
arr=[]
for i in range(m):
    arr.append(list(map(int,input().split())))

arr.sort(key= lambda x: x[2])

i=0
ans=0
for node1,node2,w in arr:
    if uf.find(node1)!=uf.find(node2):
        ans+=w
        i+=1
        uf.union(node1, node2)
        if i==n-1:
            break
print(ans)