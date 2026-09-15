class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def backtrack(i: int = 0, j: int = 0):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp.get((i, j)) is not None:
                return dp[(i, j)]
            c1, c2 = text1[i], text2[j]
            if c1 == c2:
                dp[(i, j)] = 1 + backtrack(i+1, j+1)
                return dp[(i, j)]

            dp[(i, j)]= max(backtrack(i, j+1), backtrack(i+1, j), backtrack(i+1, j+1))
            return dp[(i, j)]
        return backtrack()
        