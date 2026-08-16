class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def climb(s: int = 0):
            if s > n:
                return 0
            if s == n:
                return 1
            if dp.get(s + 1) is None:
                dp[s + 1] = climb(s+1)
            if dp.get(s + 2) is None:
                dp[s + 2] = climb(s+2)
            return dp[s+1] + dp[s + 2]
        
        return climb()
        