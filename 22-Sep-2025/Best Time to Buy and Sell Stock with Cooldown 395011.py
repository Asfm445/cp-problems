# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        memo={}

        def rec(i=0,bought=None,cooldown=False):
            if i>=len(prices):
                return 0
            if cooldown:
                return rec(i+1)
            if (i,bought) not in memo:
                if bought is None:
                    ans=max(rec(i+1,bought=prices[i]),rec(i+1))
                else:
                    profit=prices[i]-bought
                    if profit>=0:
                        ans=max(profit+rec(i+1,cooldown=True),rec(i+1,bought))
                    else:
                        ans=rec(i+1,bought)
                memo[(i,bought)]=ans
            return memo[(i,bought)]
        return rec()
            
            

        