class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i: int = 0, prev_index: int = -1):
            if i >= len(nums):
                return 0

            if dp.get((i+1, prev_index)) is None:
                dp[(i+1, prev_index)] = dfs(i+1, prev_index)

            if prev_index > -1 and nums[i] <= nums[prev_index]:
                return dp[(i+1, prev_index)]

            if dp.get((i+1, i)) is None:
                dp[(i+1, i)] = 1 + dfs(i+1, i)

            return max(dp[(i+1, prev_index)], dp[(i+1, i)])

        return dfs()


            