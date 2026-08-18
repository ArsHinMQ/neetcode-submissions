class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def calc(i: int = 0, limit: int = len(nums) - 1):
            if i >= limit:
                return 0

            if dp.get(i+1) is None:
                dp[i+1] = calc(i+1, limit)
            if dp.get(i+2) is None:
                dp[i+2] = calc(i+2, limit)

            return max(nums[i] + dp[i+2], dp[i+1])

        if len(nums) == 1:
            return nums[0]
        
        r1 = calc(0, len(nums) - 1)
        dp = {}
        r2 = calc(1, len(nums))
        return max(r1, r2)