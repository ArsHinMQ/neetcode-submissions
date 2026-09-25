class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = max(nums)
        cur_max = 0

        global_min = min(nums)
        cur_min = 0
        for n in nums:
            cur_max = max(cur_max + n, n)
            global_max = max(cur_max, global_max)

            cur_min = min(n, cur_min + n)
            global_min = min(global_min, cur_min)

        return max(sum(nums) - global_min, global_max) if global_max > 0 else global_max