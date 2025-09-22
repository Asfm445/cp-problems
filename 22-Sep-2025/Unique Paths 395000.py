# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    memo=defaultdict(int)
    def uniquePaths(self, m: int, n: int) -> int:
        if min(m,n)==0:
            self.memo[(m,n)]=0
        elif min(m,n)==1:
            self.memo[(m,n)]=1
        if not (m,n) in self.memo:
            self.memo[(m,n)]= self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        return self.memo[(m,n)]