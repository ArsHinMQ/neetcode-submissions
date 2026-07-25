class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = 0
        l = 0
        res = None
        for r, n in enumerate(nums):
            prefix += n
            while prefix >= target:
                res = min(res, r - l + 1) if res is not None else r - l + 1
                prefix -= nums[l]
                l += 1
        return res if res is not None else 0
            
        