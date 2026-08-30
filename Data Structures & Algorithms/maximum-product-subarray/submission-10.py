class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini = nums[0]
        maxi = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]

            temp = mini
            mini = min(mini*n, n, maxi*n)
            maxi = max(maxi*n, n, temp*n)
            res = max(res, maxi)
        return res