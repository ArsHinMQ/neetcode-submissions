class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def backtrack(i: int, subset: str):
            if len(subset) == len(t):
                return 1
            elif (i, subset) in dp:
                return dp[(i, subset)]
            elif i >= len(s):
                return 0

            if s[i] != t[len(subset)]:
                dp[(i, subset)] = backtrack(i+1, subset)
            else:
                dp[(i, subset)] = backtrack(i+1, subset+s[i]) + backtrack(i+1, subset)
            return dp[(i, subset)]

        return backtrack(0, "")

        