# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        dp=defaultdict(set)

        dp[stones[1]]={1}

        if stones[1]>1:
            return False

        for i in range(2,len(stones)):
            for j in range(i):
                dis=stones[i]-stones[j]
                if dis in dp[stones[j]]:
                    dp[stones[i]].add(dis)
                elif dis-1 in dp[stones[j]]:
                    dp[stones[i]].add(dis)
                elif dis+1 in dp[stones[j]]:
                    dp[stones[i]].add(dis)
        if len(dp[stones[-1]])==0:
            return False
        # print(dp)
        return True
            
        