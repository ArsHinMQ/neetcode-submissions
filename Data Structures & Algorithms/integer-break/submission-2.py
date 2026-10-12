class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def break_down(rem: int):
            if rem in dp:
                return dp[rem]
            if rem <= 2:
                return 1
            l = 2
            r = rem - 2
            max_prod = r * l
            while l <= r:
                max_prod = max(max_prod, l*r, l * break_down(r))
                l += 1
                r -= 1
            dp[rem] = max_prod
            return max_prod
        return break_down(n)
            
        