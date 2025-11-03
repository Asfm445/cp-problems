# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod=10**9+7
        diff=int(math.fabs(endPos-startPos))
        add=k-diff
        print(add,diff)
        if add<0 or add%2==1:
            return 0
        add//=2
        diff+=1
       


        m=2*add+diff+2
        print(add,diff,m)

        dp=[[0 for _ in range((m))] for _ in range(k)]
        # dp[0][]
        if startPos<=endPos:
            dp[0][m-add-1]=1
            dp[0][m-add-3]=1
            # print(dp)
        else:
            # print(dp)
            dp[0][add]=1
            dp[0][add+2]=1


        for i in range(1,k):
            for j in range(1,m-1):

                dp[i][j]=(dp[i-1][j-1]%mod+dp[i-1][j+1]%mod)%mod
                # print(i,j,len(dp),len(dp[0]))
                # print(dp)
        # print(dp)
        ans=dp[k-1][add+1] if startPos<=endPos else dp[k-1][m-add-2]
        return ans%mod

        