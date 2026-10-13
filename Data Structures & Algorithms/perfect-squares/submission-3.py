class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def bfs(rem: int):
            if rem in dp:
                return dp[rem]
            res = rem
            for o in range(math.ceil(rem/2), 0, -1):
                if o * o > rem:
                    continue
                res = min(res, 1 + bfs(rem-(o*o)))
            dp[rem] = res
            return res

            

        return bfs(n)