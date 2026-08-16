class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def calc(i: int = 0):
            if i >= len(nums):
                return 0
            if dp.get(i+2) is None:
                dp[i+2] = calc(i+2)
            if dp.get(i+3) is None:
                dp[i+3] = calc(i+3)
            return nums[i] + max(dp[i+2], dp[i+3])
        res = 0
        for i in range(len(nums)):
            res = max(res, calc(i))

        return res

        