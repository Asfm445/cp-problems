# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0:
                    dp[i][j]=matrix[i][j]
                elif j==0:
                    dp[i][j]= matrix[i][j]+min(dp[i-1][j+1],dp[i-1][j])
                elif j==len(matrix[0])-1:
                    dp[i][j]= matrix[i][j]+min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j]=matrix[i][j]+min(dp[i-1][j-1],dp[i-1][j+1],dp[i-1][j])

        # print(dp)
        
        return min(dp[len(matrix)-1])


