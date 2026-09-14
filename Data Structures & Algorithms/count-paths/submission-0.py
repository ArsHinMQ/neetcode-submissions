class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def backtrack(r: int = 0, c: int = 0):
            if r == n - 1 and c == m - 1:
                return 1
            elif r >= n or c >= m:
                return 0

            if not dp.get((r, c)):
                dp[(r, c)] = backtrack(r+1, c) + backtrack(r, c+1)
            return dp[(r, c)]
        return backtrack()