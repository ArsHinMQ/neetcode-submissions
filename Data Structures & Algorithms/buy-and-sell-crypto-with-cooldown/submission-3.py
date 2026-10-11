class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def invest(i: int, cur: int | None = None):
            if i >= len(prices):
                return 0
            if (i, cur) in dp:
                return dp[(i, cur)]
            if cur is None:
                o1 = invest(i+1, i)
            else:
                o1 = (prices[i] - prices[cur]) + invest(i+2, None)
            dp[(i, cur)] = max(o1, invest(i+1, cur))
            return dp[(i, cur)]
        return invest(0)
        