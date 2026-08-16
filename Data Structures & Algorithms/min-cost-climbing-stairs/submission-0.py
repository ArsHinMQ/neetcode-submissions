class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        n = len(cost)
        def climb(i: int = 0):
            if i >= n:
                return 0
            if dp.get(i+1) is None:
                dp[i+1] = climb(i+1)
            if dp.get(i+2) is None:
                dp[i+2] = climb(i+2)
            return cost[i] + min(dp[i+1], dp[i+2])
        
        return min(climb(0), climb(1))
        