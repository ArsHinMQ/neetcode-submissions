class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def backtrack(i: int = 0, c: int = -1):
            if i >= len(prices):
                return 0
            if dp.get((i, c)) is not None:
                pass
            elif c == -1:
                dp[(i, c)] = max(backtrack(i+1, -1), backtrack(i+1, i))
            else:
                profit = prices[i] - prices[c]

                dp[(i, c)] = max(profit + backtrack(i+2, -1), backtrack(i+1, c))
            return dp[(i, c)]
        
        return backtrack()