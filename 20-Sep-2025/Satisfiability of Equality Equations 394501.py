# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        # If x hasn't been seen before, initialize it
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        
        # First, process all equality equations to build connected components.
        for eq in equations:
            if eq[1] == '=':
                a = eq[0]
                b = eq[3]
                uf.union(a, b)
        
        # Then, check all inequality equations.
        for eq in equations:
            if eq[1] == '!':
                a = eq[0]
                b = eq[3]
                # If two unequal variables are in the same component, it's invalid.
                if uf.find(a) == uf.find(b):
                    return False
        
        return True