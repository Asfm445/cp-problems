# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        j=1
        m=strs[0]
        while i<len(strs):
            if strs[i-1][0:j] == strs[i][0:j] and j<=min(len(strs[i]),len(strs[i-1])):
                j+=1
            else:
                if strs[i-1][0:j-1]<m:
                    m=strs[i][0:j-1] 
                i+=1
                j=0
        return str(m)
  
        