# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # dp[i][0] = max profit on day i when not holding a stock
        # dp[i][1] = max profit on day i when holding a stock
        dp = [[0] * 2 for _ in range(n)]
        
        # Initial state
        dp[0][0] = 0  # Not holding stock on day 0
        dp[0][1] = -prices[0]  # Holding stock on day 0 (cost of buying it)
        
        for i in range(1, n):
            # If not holding stock today, either we didn't hold it yesterday or we sold it today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            # If holding stock today, either we held it yesterday or we bought it today
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        # The answer will be in dp[n-1][0], as we want to end up not holding any stock
        return dp[n-1][0]

        