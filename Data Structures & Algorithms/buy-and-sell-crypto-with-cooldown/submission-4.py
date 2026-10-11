class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def invest(i: int, buying: bool = True):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            skip = invest(i+1, buying)
            if buying:
                action = -prices[i] + invest(i+1, False)
            else:
                action = prices[i] + invest(i+2, True)
            dp[(i, buying)] = max(action, skip)
            return dp[(i, buying)]
        return invest(0)
        