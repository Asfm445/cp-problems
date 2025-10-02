# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp=[0]*len(questions)
        dp[-1]=questions[-1][0]

        for i in range(len(questions)-2,-1,-1):
            pt,nx=questions[i]
            nxt=0
            if i+nx+1<len(questions):
                nxt=dp[i+nx+1]
            # print(nxt,i+nx)
            dp[i]=max(dp[i+1],nxt+pt)
        # print(dp)
        return dp[0]

        
            
        