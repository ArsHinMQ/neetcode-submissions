class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True
        def backtrack(i: int):
            if i <= 0:
                return
            if s[i] == "1":
                return
            if dp[i]:
                return
            dp[i] = True
            for j in range(i-minJump, i-maxJump-1, -1):
                backtrack(j)

        backtrack(len(s) - 1)
        for i in range(minJump, maxJump+1):
            if dp[i]:
                return True
        return False
