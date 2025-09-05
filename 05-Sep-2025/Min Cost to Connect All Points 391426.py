# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self):
        self.root =defaultdict(tuple)
    def find(self, X):
        if not X in self.root:
            self.root[X]=X
        if X == self.root[X]:
            return X
        self.root[X]=self.find(self.root[X])
        return self.find(self.root[X])
    def union(self, X, Y):
        rootX, rootY = self.find(X), self.find(Y)
        if rootX != rootY:
            root=min(rootX,rootY)
            self.root[rootX]=root
            self.root[rootY]=root


class Solution(object):
    def minCostConnectPoints(self, points):
        dis=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                length=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                dis.append([points[i],points[j],length])
        dis.sort(key=lambda x: x[2])
        ans=0
        num=0
        dsu=UnionFind()
        for p1,p2,length in dis:
            p1_tup=(p1[0],p1[1])
            p2_tup=(p2[0],p2[1])
            if dsu.find(p1_tup)!=dsu.find(p2_tup):
                dsu.union(p1_tup,p2_tup)
                ans+=length
                num+=1
                if num==len(points)-1:
                    break
        return ans
        """
        :type points: List[List[int]]
        :rtype: int
        """
        