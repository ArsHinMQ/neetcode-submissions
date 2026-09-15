class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def backtrack(i: int = 0, buying: bool = True):
            if i >= len(prices):
                return 0
            if dp.get((i, buying)):
                return dp[(i, buying)]
            cooldown = backtrack(i+1, buying)
            if buying:
                dp[(i, buying)] = max(-prices[i] + backtrack(i+1, not buying), cooldown)
            else:
                dp[(i, buying)] = max(prices[i] + backtrack(i+2, not buying), cooldown)
            return dp[(i, buying)]

        return backtrack()