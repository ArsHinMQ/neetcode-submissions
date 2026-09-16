class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i: int = 0, s: int = 0):
            if (i, s) in dp:
                return dp[(i, s)]
            if i >= len(nums):
                if s == target:
                    dp[(i, s)] = 1
                else:
                    dp[(i, s)] = 0
            else:
                dp[(i, s)] = backtrack(i+1, s+nums[i]) + backtrack(i+1, s-nums[i])
            return dp[(i, s)]
        return backtrack()
        