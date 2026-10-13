class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def bs(rem: int):
            l = 0
            r = rem
            res = 1
            while l < r:
                m = (l+r) // 2
                if m * m == rem:
                    return m
                elif m > rem:
                    r = m
                else:
                    l = m + 1
                    res = max(res, m)
            return res

        def bfs(rem: int):
            if rem in dp:
                return dp[rem]
            res = rem
            for o in range(bs(rem), 0, -1):
                if o * o > rem:
                    continue
                res = min(res, 1 + bfs(rem-(o*o)))
                if res == 1:
                    break
            dp[rem] = res
            return res

            

        return bfs(n)