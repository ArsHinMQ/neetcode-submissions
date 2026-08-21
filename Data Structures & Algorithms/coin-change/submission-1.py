class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, len(dp)):
            for c in coins:
                diff = i - c
                if diff == 0:
                    dp[i] = 1
                elif diff < 0:
                    continue
                else:
                    if dp[diff] == -1:
                        continue
                    dp[i] = min(1+dp[diff], dp[i]) if dp[i] > 0 else 1+dp[diff]
            if dp[i] == 0:
                dp[i] = -1
        return dp[-1]