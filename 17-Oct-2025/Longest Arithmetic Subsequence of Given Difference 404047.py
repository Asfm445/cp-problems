# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        d=defaultdict(lambda : 1)

        for i in arr:
            diff=i-difference
            if diff in d:
                d[i]=d[diff]+1
            else:
                d[i]=1
        print(d)
        return max(d.values()) 
        