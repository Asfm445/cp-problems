# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[[1]]
        for i in range(rowIndex):
            arr=[]
            for j in range(len(ans[-1])+1):
                if not j==0 and not j==len(ans[-1]):
                    arr.append(ans[-1][j]+ans[-1][j-1])
                if j==0:
                    arr.append(ans[-1][j])
                if j==len(ans[-1]):
                    arr.append(ans[-1][j-1])
            ans.append(arr)
            arr=[]
        return ans[-1]