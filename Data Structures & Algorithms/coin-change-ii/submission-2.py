class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}
        def backtrack(i: int = 0, s: int = 0):
            if dp.get((i, s)) is not None:
                return dp[(i, s)]
            elif s == amount:
                dp[(i, s)] = 1
            elif s > amount:
                dp[(i, s)] = 0
            elif i >= len(coins):
                return 0
            else:
                dp[(i, s)] = backtrack(i, s+coins[i]) + backtrack(i+1, s)
            return dp[(i, s)]
        return backtrack()