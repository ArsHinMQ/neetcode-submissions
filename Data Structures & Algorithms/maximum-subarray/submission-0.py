class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = s
        for i in range(1, len(nums)):
            n = nums[i]
            if n > s + n:
                s = n
            else:
                s += n
            res = max(res, s)   
            
        return res
        