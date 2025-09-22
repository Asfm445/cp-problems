# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = defaultdict(int)


        def solve(x):
            if x < 0:
                return float("inf")
            if x == 0:
                return 0
            best = float("inf")
            for i in coins:
                if x - i not in d:
                    d[x - i] = solve(x - i) + 1
                best = min(best, d[x - i])
            return best
        ans=solve(amount)
        if ans==float('inf'):
            return -1
        return ans
        