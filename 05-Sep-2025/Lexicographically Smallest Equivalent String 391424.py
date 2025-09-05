# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self):
        self.root =defaultdict(str)
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
    def smallestEquivalentString(self, s1, s2, baseStr):
        uf=UnionFind()
        for i in range(len(s1)):
            uf.union(s1[i],s2[i])
        ans=[]
        for char in baseStr:
            ans.append(uf.find(char))
        return ''.join(ans)
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        