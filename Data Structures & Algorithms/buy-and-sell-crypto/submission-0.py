class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        profit = 0
        for r in prices:
            if r < l:
                l = r
            else:
                profit = max(profit, r - l)
        return profit

            
        