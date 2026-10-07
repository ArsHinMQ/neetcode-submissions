class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(needed: int = target):
            if needed < 0:
                return 0
            elif needed == 0:
                return 1

            total = 0
            for i in range(len(nums)):
                nneeded = needed - nums[i]
                if nneeded in dp:
                    total += dp[nneeded]
                else:
                    dp[nneeded] = backtrack(nneeded)
                    total += dp[nneeded]
            return total
        r = backtrack()
        return r
            

        